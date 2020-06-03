# $0$ networkname
# $1$ buf_networkname
# $2$ cond_rule_str

ruleset n:Machines do

    choose midx:$0$[n] do
        alias mach:$0$[n] do
        alias msg:mach[midx] do
          rule "Receive $0$"
            !isundefined(msg.mtype)
          ==>
            if (ENABLE_QS) then
              if PushQueue($1$, n, msg) then
                MultiSetRemove(midx, mach);
              endif;
            else
              -- Without input queues
$2$
            endif;
          endrule;
        endalias;
        endalias;
    endchoose;

endruleset;