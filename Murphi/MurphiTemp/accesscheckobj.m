# $0$ Total number of machines
# $1$ kmachines
# $2$ kaddress

v_MACH_MULTISET: multiset[$0$] of $1$;
cnt_MACH_MULTISET: 0..$0$;

Access_machine: record
  store: array[$2$] of v_MACH_MULTISET;
  load: array[$2$] of v_MACH_MULTISET;
end;