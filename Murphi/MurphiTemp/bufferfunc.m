# $0$ archname
# $1$ machineset
# $2$ maxindex
# $3$ DeferType
# $4$ DeferVarName

procedure $0$_$4$_PushDeferMsg(msg:$3$; adr: Address; m:$1$);
begin
	alias cle: $0$[m].CL[adr] do
	alias q: cle.$4$.Queue do
	alias qind: cle.$4$.QueueInd do

	if (qind<=$2$) then
      q[qind]:=msg;
      qind:=qind+1;
    endif;

	endalias;
	endalias;
	endalias;
end;

function $0$_$4$_PopDeferMsg(adr: Address; m:$1$) : $3$;
var
  msg: $3$;
begin
  alias cle: $0$[m].CL[adr] do
  alias q: cle.$4$.Queue do
  alias qind: cle.$4$.QueueInd do
  undefine msg;

  if !isundefined(q[0].mtype) then
    msg := q[0];
  endif;

  for i := 0 to qind-1 do
      if i < qind-1 then
        q[i] := q[i+1];
      else
        undefine q[i];
      endif;
    endfor;
    qind := qind - 1;

  return msg;

  endalias;
  endalias;
  endalias;
end;

