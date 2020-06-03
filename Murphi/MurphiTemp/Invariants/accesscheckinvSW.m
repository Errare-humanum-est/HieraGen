# $0$ kaddress

invariant "Single Writer"
  forall a:$0$ do
    !MultiSetCount(i:g_access.store[a], true) > 1
  endforall;

