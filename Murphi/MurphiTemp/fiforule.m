# $0$ fifobuffer
# $1$ cond_rule_str

ruleset n:Machines do
  alias p:$0$[n] do

      rule "$0$"
        (p.QueueInd>0)
      ==>
        alias msg:p.Queue[0] do
$1$
        endalias;

      endrule;
  endalias;
endruleset;