# $0$ cache_id
# $1$ cache_line_id

/* Tries to serve the access */
function cpu_try_access_$0$(var cpu: MACH_CPU): boolean;
var instr: INSTR;
begin
  instr := GetInstr(cpu);

  alias adr:instr.adr do
  alias cache: cpu.cache do
  alias cle:i_$0$[cache].CL[adr] do

  /* Load operation */
  if instr.access = load & (Test_store(adr, cache) | Test_load(adr, cache)) then
    UpdateVal(cpu, cle.cl$1$);
    return true;
  endif;

  /* Store operation */
  if instr.access = store & Test_store(adr, cache) then
    cle.cl$1$ := instr.cl;
    return true;
  endif;

  return false;
  endalias;
  endalias;
  endalias;
end;
