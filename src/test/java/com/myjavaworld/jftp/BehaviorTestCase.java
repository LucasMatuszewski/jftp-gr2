package com.myjavaworld.jftp;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Comparator;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.TimeUnit;
import junit.framework.TestCase;

/** Real synthetic state, installed before any JFTP class initialization. */
public abstract class BehaviorTestCase extends TestCase {
    protected static final Path PROFILE = createProfile();
    protected Path files;

    private static Path createProfile() {
        try {
            Path home = Files.createTempDirectory("jftp-characterization-");
            System.setProperty("user.home", home.toString());
            return home;
        } catch (Exception failure) {
            throw new ExceptionInInitializerError(failure);
        }
    }

    protected void setUp() throws Exception {
        files = Files.createTempDirectory(PROFILE, "files-");
    }

    protected File dataFile(String name) {
        return PROFILE.resolve(".jftp/data").resolve(name).toFile();
    }

    protected void tearDown() throws Exception {
        try (java.util.stream.Stream<Path> paths = Files.walk(files)) {
            for (Path path : (Iterable<Path>) paths.sorted(Comparator.reverseOrder())::iterator) {
                Files.delete(path);
            }
        }
    }

    protected RemoteHost favorite(String name) {
        RemoteHost host = new RemoteHost(name, "127.0.0.1", 2121, "synthetic", "test-only", "account");
        host.setInitialLocalDirectory(files.toString());
        host.setInitialRemoteDirectory("/synthetic");
        host.setCommands("TYPE I\nNOOP");
        host.setPassive(false);
        return host;
    }

    protected void readInAnotherJvm(String operation) throws Exception {
        File java = new File(System.getProperty("java.home"), "bin/java.exe");
        if (!java.isFile()) { java = new File(System.getProperty("java.home"), "bin/java"); }
        Path log = files.resolve(operation + ".log");
        Process child = new ProcessBuilder(java.toString(), "-Djava.awt.headless=true",
                "-Duser.home=" + PROFILE, "-cp",
                System.getProperty("surefire.test.class.path", System.getProperty("java.class.path")),
                StateProbe.class.getName(), operation).redirectErrorStream(true).redirectOutput(log.toFile()).start();
        try {
            assertTrue("Child JVM timeout", child.waitFor(30, TimeUnit.SECONDS));
            assertEquals(new String(Files.readAllBytes(log), StandardCharsets.UTF_8), 0, child.exitValue());
        } finally {
            if (child.isAlive()) { child.destroyForcibly(); child.waitFor(5, TimeUnit.SECONDS); }
        }
    }
}
