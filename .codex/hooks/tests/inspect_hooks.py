"""Read native hook discovery/trust metadata through the local app-server RPC.

No model call, config write, credential read, or trust change is performed.
"""
import json
from pathlib import Path
import queue
import shutil
import subprocess
import threading


class AppServer:
    """Native RPC test client; optional evidence contains this session only."""

    def __init__(self, extra_args=(), environment=None, evidence=None):
        self.messages = queue.Queue()
        self.log = (evidence / "events.jsonl").open("w", encoding="utf-8") if evidence else None
        self.errors = (evidence / "stderr.log").open("w", encoding="utf-8") if evidence else None
        self.process = subprocess.Popen([shutil.which("codex"), *extra_args, "app-server", "--stdio"],
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                        stderr=self.errors or subprocess.DEVNULL,
                                        text=True, encoding="utf-8", env=environment)
        self.reader = threading.Thread(target=self.read, daemon=True)
        self.reader.start()

    def read(self):
        for line in self.process.stdout:
            if self.log:
                self.log.write(line)
                self.log.flush()
            self.messages.put(json.loads(line))
        self.messages.put(None)

    def receive(self, timeout=30):
        message = self.messages.get(timeout=timeout)
        if message is None:
            raise RuntimeError("App-server exited before replying; inspect stderr evidence")
        return message

    def send(self, message):
        self.process.stdin.write(json.dumps(message) + "\n")
        self.process.stdin.flush()

    def rpc(self, identifier, method, params):
        self.send({"id": identifier, "method": method, "params": params})
        while True:
            message = self.receive()
            if message.get("id") == identifier:
                if "error" in message:
                    raise RuntimeError(message["error"])
                return message["result"]

    def __enter__(self):
        self.rpc(1, "initialize", {"clientInfo": {"name": "pom-hook-inspect", "version": "1"},
                                   "capabilities": {"experimentalApi": True}})
        self.send({"method": "initialized"})
        return self

    def __exit__(self, *unused):
        self.process.stdin.close()
        try:
            self.process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            self.process.terminate()
            self.process.wait(timeout=10)
        self.reader.join(timeout=5)
        self.process.stdout.close()
        if self.log:
            self.log.close()
        if self.errors:
            self.errors.close()


def inspect_hooks(root, extra_args=()):
    with AppServer(extra_args) as server:
        return server.rpc(2, "hooks/list", {"cwds": [str(root)]})["data"][0]


if __name__ == "__main__":
    print(json.dumps(inspect_hooks(Path(__file__).resolve().parents[3]), indent=2))
