# $0$ networkname
# $1$ cnt_network
# $2$ buf_networkname
# $3$ cond_rule_str

ruleset n:Machines do
    alias msg:$0$[n][0] do
      rule "Receive $0$"
        $1$[n] > 0
      ==>
        -- With input queues
        if (ENABLE_QS) then
          if PushQueue($2$, n, msg) then
            Pop_$0$(n);
          endif;
        else
        -- Without input queues
$3$
        endif;
      endrule;
    endalias;

endruleset;