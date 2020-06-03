# $0$ machname

function LockTest(): boolean;
begin
  if mutex.mutex = unlocked then
    return true;
  endif;
  return false;
end;

procedure LockAcquire(m: $0$);
begin
  mutex.mutex := locked;
  mutex.mach := m;
end;

function LockRelease(m: $0$): boolean;
begin
  if mutex.mutex = locked & mutex.mach = m then
    mutex.mutex := unlocked;
    mutex.mach := undefined;
    return true;
  endif;
  return false;
end;

procedure LockReset();
begin
  mutex.mutex := unlocked;
  mutex.mach := undefined;
end;
