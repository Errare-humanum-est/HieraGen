# $0$ networkname

procedure Broadcast_$0$(var msg: Message;);
begin
      for iSV:Machines do
          msg.dst := iSV;
          Send_$0$(msg);
      endfor;
end;