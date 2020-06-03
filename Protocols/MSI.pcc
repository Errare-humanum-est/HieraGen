# NrCaches 3

Network { Ordered fwd;    //FwdGetS, FwdGetM, Inv, PutAck
          Ordered resp; // Data, InvAck
          Ordered req;   //GetS, GetM, PutM
          };

Cache {
    State I;
    Data cl;
    int[0..NrCaches] acksReceived = 0;
    int[0..NrCaches] acksExpected = 0;
} set[NrCaches] cache;

Directory {
    State I;
    Data cl;
    set[NrCaches] ID cache;
    ID owner;
} directory;

Message Request{};

Message Ack{};

Message Resp{
    Data cl;
};

Message RespAck{
    Data cl;
    int[0..NrCaches] acksExpected;
};

Architecture cache {

    Stable{I, S, M}

    // I ////////////////////////////////////////////////////////
    Process(I, load, State){
        msg = Request(GetS, ID, directory.ID);
        req.send(msg);

        await{
            when GetS_Ack:
                cl=GetS_Ack.cl;
                State = S;
                break;
        }
    }

    Process(I, store, State){
        msg = Request(GetM, ID, directory.ID);
        req.send(msg);
        acksReceived = 0;

        await{
            when GetM_Ack_D:
                cl=GetM_Ack_D.cl;
                State = M;
                break;

            when GetM_Ack_AD:
                cl=GetM_Ack_AD.cl;
                acksExpected = GetM_Ack_AD.acksExpected;

                if acksExpected == acksReceived{
                    State = M;
                    break;
                }

                await{
                    when Inv_Ack:
                        acksReceived = acksReceived + 1;

                        if acksExpected == acksReceived{
                            State = M;
                            break;
                        }
                    }

            when Inv_Ack:
                acksReceived = acksReceived + 1;
        }
    }

    // S ////////////////////////////////////////////////////////
    Process(S, load, S){}

    Process(S, store, State){
        msg = Request(GetM, ID, directory.ID);
        req.send(msg);
        acksReceived = 0;

        await{
            when GetM_Ack_D:
                State = M;
                break;

            when GetM_Ack_AD:
                acksExpected = GetM_Ack_AD.acksExpected;

                if acksExpected == acksReceived{
                    State = M;
                    break;
                }

                await{
                    when Inv_Ack:
                        acksReceived = acksReceived + 1;

                        if acksExpected == acksReceived{
                            State = M;
                            break;
                        }
                    }

            when Inv_Ack:
                acksReceived = acksReceived + 1;
        }
    }

    Process(S, evict, State){
        msg = Request(PutS, ID, directory.ID);
        req.send(msg);

        await{
            when Put_Ack:
                State = I;
                break;
        }
    }

    Process(S, Inv, I){
        msg = Resp(Inv_Ack, ID, Inv.src, cl);
        resp.send(msg);
    }


    // M ////////////////////////////////////////////////////////
    Process(M, load){
    }

    Process(M, store, M){}

    Process(M, Fwd_GetM, I){
        msg = Resp(GetM_Ack_D, ID, Fwd_GetM.src, cl);
        resp.send(msg);
    }

    Process(M, Fwd_GetS, S){
        msg = Resp(GetS_Ack, ID, Fwd_GetS.src, cl);
        resp.send(msg);
        msg = Resp(WB, ID, directory.ID, cl);
        resp.send(msg);
    }

    Process(M, evict, State){
        msg = Resp(PutM, ID, directory.ID, cl);
        req.send(msg);

        await{
            when Put_Ack:
                State = I;
                break;
        }
    }

}

Architecture directory {

    Stable{I, S, M}

    // I ////////////////////////////////////////////////////////
    Process(I, GetS, S){
       cache.add(GetS.src);
       msg = Resp(GetS_Ack, ID, GetS.src, cl);
       resp.send(msg);
    }

    Process(I, GetM, M){
        msg = Resp(GetM_Ack_D, ID, GetM.src, cl);
        resp.send(msg);
        owner = GetM.src;
    }

    // S ////////////////////////////////////////////////////////
    Process(S, GetS){
       cache.add(GetS.src);
       msg = Resp(GetS_Ack, ID, GetS.src, cl);
       resp.send(msg);
    }

    Process(S, GetM){
       if cache.contains(GetM.src){
           cache.del(GetM.src);
           if cache.count() == 0{
                msg = Resp(GetM_Ack_D, ID, GetM.src, cl);
                resp.send(msg);
                State=M;
                break;
           } else{
               msg = RespAck(GetM_Ack_AD, ID, GetM.src, cl, cache.count());
               resp.send(msg);
               msg = Ack(Inv, GetM.src, GetM.src);
               fwd.mcast(msg, cache);
               State=M;
               break;
           }
           owner = GetM.src;
           cache.clear();
           break;
       } else {
           msg = RespAck(GetM_Ack_AD, ID, GetM.src, cl, cache.count());
           resp.send(msg);
           State=M;
           msg = Ack(Inv, GetM.src, GetM.src);
           fwd.mcast(msg, cache);
           owner = GetM.src;
           cache.clear();
           break;
       }
    }

    Process(S, PutS){
       msg = Ack(Put_Ack, ID, PutS.src);
       fwd.send(msg);
       cache.del(PutS.src);

       if cache.count() == 0{
            State=I;
            break;
       }
    }

    Process(S, PutM){
       msg = Ack(Put_Ack, ID, PutM.src);
       fwd.send(msg);
       cache.del(PutM.src);

       if cache.count() == 0{
            State=I;
            break;
       }
    }


    // M ////////////////////////////////////////////////////////
    Process(M, GetS){
       msg = Request(Fwd_GetS, GetS.src, owner);
       fwd.send(msg);
       cache.add(GetS.src);
       cache.add(owner);

       await{
            when WB:
                if WB.src == owner{
                    cl = WB.cl;
                    State=S;
                }
       }

    }

    Process(M, GetM){
       msg = Request(Fwd_GetM, GetM.src, owner);
       fwd.send(msg);
       owner = GetM.src;
    }

    Process(M, PutM){
       msg = Ack(Put_Ack, ID, PutM.src);
       fwd.send(msg);
       cache.del(PutM.src);

       if owner == PutM.src{
            cl = PutM.cl;
            State=I;
       }
    }

}