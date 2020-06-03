# $0$ kaddress

invariant "Exclusive Write"
  forall a:$0$ do
    MultiSetCount(i:g_access.store[a], true) > 0
    ->
    MultiSetCount(i:g_access.load[a], true) = 0
  endforall;