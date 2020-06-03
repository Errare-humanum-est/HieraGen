# $0$ cache_id

  /* Try to serve access */
  if ismember(cpu.cache, OBJSET_$0$) then
    if cpu_try_access_$0$(cpu) then
      PopInstr(cpu);
    else
      /* If access cannot be served issue request by cache */
        access_$0$(cpu);
      endif;
  endif;