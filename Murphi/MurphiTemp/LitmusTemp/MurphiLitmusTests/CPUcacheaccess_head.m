# $0$ cache_id

/* Issue Cache request to update */
procedure access_$0$(var cpu: MACH_CPU);
var instr: INSTR;
begin
  instr := GetInstr(cpu);
  alias adr:instr.adr do
  alias cache: cpu.cache do
  alias cle:i_$0$[cache].CL[adr] do
  alias access: instr.access do
