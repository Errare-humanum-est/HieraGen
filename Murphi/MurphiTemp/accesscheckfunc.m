# $0$ kaddress
# $1$ kmachines

procedure Set_store_exe(adr: $0$; n:$1$);
begin
  alias g_st:g_access.store[adr] do
    if MultiSetCount(i:g_st, g_st[i] = n) = 0 then
      MultiSetAdd(n, g_st);
    endif;
  endalias;
end;

procedure Clear_store(adr: $0$; n:$1$);
begin
  alias g_st:g_access.store[adr] do
    if MultiSetCount(i:g_st, g_st[i] = n) = 1 then
      MultiSetRemovePred(i:g_st, g_st[i] = n);
    endif;
  endalias;
end;

procedure Set_load_exe(adr: $0$; n:$1$);
begin
  alias g_st:g_access.load[adr] do
    if MultiSetCount(i:g_st, g_st[i] = n) = 0 then
      MultiSetAdd(n, g_st);
    endif;
  endalias;
end;

procedure Clear_load(adr: $0$; n:$1$);
begin
  alias g_st:g_access.load[adr] do
    if MultiSetCount(i:g_st, g_st[i] = n) = 1 then
      MultiSetRemovePred(i:g_st, g_st[i] = n);
    endif;
  endalias;
end;

procedure Set_store(adr: $0$; n:$1$);
begin
  Clear_load(adr, n);
  Set_store_exe(adr, n);
end;

procedure Set_load(adr: $0$; n:$1$);
begin
  Clear_store(adr, n);
  Set_load_exe(adr, n);
end;

procedure Clear_acc(adr: $0$; n:$1$);
begin
  Clear_store(adr, n);
  Clear_load(adr, n);
end;

procedure Reset_acc();
begin
  for a:$0$ do
    undefine g_access.store[a];
  endfor;

  for a:$0$ do
    undefine g_access.load[a];
  endfor;
end;

function Test_store(adr: Address; n:Machines): boolean;
begin
  alias g_st:g_access.store[adr] do
    if MultiSetCount(i:g_st, g_st[i] = n) = 1 then
      return true;
    endif;
  endalias;
  return false;
end;

function Test_load(adr: Address; n:Machines): boolean;
begin
  alias g_st:g_access.load[adr] do
    if MultiSetCount(i:g_st, g_st[i] = n) = 1 then
      return true;
    endif;
  endalias;
  return false;
end;