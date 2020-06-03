/* If at least one instruction stream still exists, then don't do reset */
function Check_reset(): boolean;
begin
  for i:OBJSET_CPU do
    if i_cpu[i].active = true then
      return false;
    endif;
  endfor;

  return true;
end;