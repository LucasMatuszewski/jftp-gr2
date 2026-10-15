// @exec: {"yield_time_ms": 30000, "max_output_tokens": 650000}
// RAW TEXT DELIVERY ONLY. No XML/code parsing, comparison, counting or inference.
const repo = 'C:/Users/BiuroEdukey/DEV/COURSES/Sages/jftp-gr2';
const specs = [
  {key:'a', file:'jftp.full-no-comments.xml', start:0, end:600000},
  {key:'b', file:'jftp.full-no-comments.xml', start:600000, end:1171503},
  {key:'c', file:'jftp.compressed-no-comments.xml', start:0, end:878499},
];
function utf8bytes(text) {
  let total=0;
  for (const c of text) { const n=c.codePointAt(0); total+=n<128?1:n<2048?2:n<65536?3:4; }
  return total;
}
const results = await Promise.allSettled(specs.map(async s => {
  const p=repo+'/docs/RepoMix/'+s.file;
  const result=await tools.exec_command({
    cmd:`node -e "const f=require('fs').readFileSync(process.argv[1]);process.stdout.write(f.subarray(+process.argv[2],+process.argv[3]));" '${p}' ${s.start} ${s.end}`,
    sandbox_permissions:'require_escalated',
    justification:'Deliver exact raw file text for the user-requested direct LLM review; no analysis or changes.',
    max_output_tokens:400000
  });
  if(result.exit_code!==0 || utf8bytes(result.output)!==s.end-s.start) throw new Error('Incomplete raw read: '+s.key);
  return result.output;
}));
if(results.some(r=>r.status!=='fulfilled')) throw new Error('RAW PRELOAD FAILED: a file read was incomplete');
const texts={'jftp.full-no-comments.xml':results[0].value+results[1].value,'jftp.compressed-no-comments.xml':results[2].value};
const planResult=await tools.exec_command({
  cmd:`node -e "process.stdout.write(require('fs').readFileSync(process.argv[1]));" '${repo}/docs/RepoMix/artifacts/luna-chunk-plan.json'`,
  sandbox_permissions:'require_escalated',justification:'Read the fixed transport byte ranges; no source analysis.',max_output_tokens:400000
});
if(planResult.exit_code!==0) throw new Error('Transport plan read failed');
const plan=JSON.parse(planResult.output);
let delivered=0;
for(const file of plan.files) {
  const data=texts[file.name];
  if(utf8bytes(data)!==file.bytes) throw new Error('Whole-file byte count mismatch');
  let bytes=0, index=0, startIndex=0, packetIndex=0;
  for(const char of data) {
    const n=char.codePointAt(0); bytes+=n<128?1:n<2048?2:n<65536?3:4; index+=char.length;
    const packet=file.packets[packetIndex];
    if(bytes>packet.end) throw new Error('Invalid UTF-8 transport boundary');
    if(bytes===packet.end) {
      notify('RAW FILE '+file.name+' BYTES ['+packet.start+','+packet.end+')\nBEGIN RAW TEXT\n'+data.slice(startIndex,index)+'\nEND RAW TEXT '+file.name+' '+packet.end);
      startIndex=index; packetIndex++; delivered++;
    }
  }
  if(bytes!==file.bytes || packetIndex!==file.packets.length) throw new Error('Incomplete delivery');
}
text('RAW PRELOAD COMPLETE: both complete unchanged texts delivered in '+delivered+' separate raw-text notifications. No programmatic content analysis was performed. Now compare their contents directly in the model and produce the requested final review in this SAME turn, before any further tool call or final handoff.');
