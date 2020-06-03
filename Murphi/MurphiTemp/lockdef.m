Lock: enum{
  unlocked,
  locked
};

OBJ_LOCK: record
  mutex: Lock;
  mach: Machines;
end;
