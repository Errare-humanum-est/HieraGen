  for i:OBJSET_CPU do
      undefine i_cpu[i].cache;
      i_cpu[i].active := true;
      undefine i_cpu[i].instrstr.Queue;
      i_cpu[i].instrstr.QueueInd:=0;
      i_cpu[i].instrstr.QueueCnt:=0;
  endfor;

  CPU_Cache_Map(i_cpu);
  Instr(i_cpu);