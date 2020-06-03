# $0$ Arch_name
# $1$ Machines
# $2$ state_suffix
# $3$ var_suffix
# $4$ state_def

procedure ModifyStates_$0$(Mach: $1$; Cur_state: $2$$0$; Next_state: $2$$0$);
begin
    alias p:$3$$0$[Mach] do
      for a:Address do
          if (p.CL[a].$4$ = Cur_state) then
              p.CL[a].$4$ := Next_state;
          endif;
      endfor;
    endalias;
end;