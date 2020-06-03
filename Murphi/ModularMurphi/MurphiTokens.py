class MurphiTokens:
    ssp_prefix = "SSP_"
    mutex = "mutex"

    defaccess = "none"
    defload = "load"
    defstore = "store"
    defval = "undefined"
    defset = "undefine"

    statesuf = "s_"
    vectorsuf = "v_"
    countsuf = "cnt_"
    instsuf = "i_"

    TemplateDir = "MurphiTemp"

    fconst = "const.m"

    # Lock framework
    flockdef = "lockdef.m"
    flockfunc = "lockfunc.m"

    # Access invariant framework
    faccesscheckobj = "accesscheckobj.m"
    faccesscheckvar = "accesscheckvar.m"
    faccesscheckfunc = "accesscheckfunc.m"

    ffifo = "fifo.m"
    ffifofunc = "fifofunc.m"
    ffiforule = "fiforule.m"
    ffiforuleinner = "fiforuleinner.m"
    ffifoinit = "fifoinit.m"

    fbuffer = "buffer.m"
    fbufferfunc = "bufferfunc.m"

    fdeferpushfunc = "deferpushfunc.m"
    fdeferpopfunc = "deferpopfunc.m"

    fonetwork = "onetworkfunc.m"
    forderedrule = "orderedrule.m"
    forderedruleinner = "orderedruleinner.m"
    forderedinit = "orderedinit.m"

    funetwork = "unetworkfunc.m"
    funorderedrule = "unorderedrule.m"
    funorderedruleinner = "unorderedruleinner.m"
    funorderedinit = "unorderedinit.m"

    fonetworkready = "onetworkready.m"
    funetworkready = "unetworkready.m"

    fmulticast = "multicastfunc.m"
    fbroadcast = "broadcastfunc.m"
    fvector = "vectorfunc.m"

    fmodifystate = "modifystatefunc.m"

    # Invariants
    faccesscheckinvSW = "Invariants/accesscheckinvSW.m"     # Single writer
    faccesscheckinvEW = "Invariants/accesscheckinvEW.m"     # Exclusive writer

    # Litmus Templates
    fcpuinstancegen = "LitmusTemp/CPUdefinition.m"
    fcpubufferfunc = "LitmusTemp/CPUbufferfunc.m"

    # Makefile template
    ftmpmake = "tmpmakefile"

    # Enum keywords
    kaccess = "Access"
    kmessages = "MessageType"
    kaddress = "Address"
    kcacheval = "ClValue"
    kmachines = "Machines"
    kcpu = "CPU"

    # Record keywords
    rbasemessage = "BaseMessage"
    rmessage = "Message"
    rfifo = "FIFO"
    rbuffer = "Buffer"
    rsendbuffer = "SendBuffer"

    # const
    cvalcntid = "VAL_COUNT"
    cadrcntid = "ADR_COUNT"

    SetKey = 'OBJSET_'
    EntryKey = 'ENTRY_'
    MachKey = 'MACH_'
    ObjKey = "OBJ_"
    Initval = 'INITVAL_'

    CLIdent = 'CL'

    tINITSTATE = "INITSTATE_"
    tDATA = "DATA_"

    DataDef = {
        'OBJSET_': '_PassNode',
        tINITSTATE: '_setInitState',
        tDATA: '_genData',
        'ID_': '_genID',
        'INT_': '_genInt',
        'BOOL_': '_genBool',
        'MSG_': '_genMSG',
    }

    defmsgname = "msg"

    cadr = "adr"
    cmach = "m"             # if you change this please change the template files too
    ccle = "cle"
    cdle = "dle"
    cmtype = "mtype"
    cinmsg = "inmsg"
    cbasemsg = "basemsg"

    madr = {cadr: kaddress}
    mtype = {cmtype: kmessages}
    msrc = {"src": kmachines}
    mdst = {"dst": kmachines}
    BaseMsg = [madr, mtype, msrc, mdst]

    # Machine instances
    iState = 'State'
    iID = 'ID'
    iFifo = 'Buffer'
    iAccess = 'Perm'

    # Interconnect parameters
    cordered = "O_NET_MAX"
    cunordered = "U_NET_MAX"
    ordered = "Ordered"
    orderedcnt = "Orderedcnt"
    k_onetwork = "onet_"
    unordered = "Unordered"
    k_unetwork = "unet_"

    # FIFOs
    k_fifo = "buf_"

    SetFuncDef = {
        'add': '_genVectAdd',
        'del': '_genVectDel',
        'clear': '_genVectClear',
        'contains': '_genVectCont',
        'empty': '_genVectEmpty',
        'count': '_genVectCnt',
    }

    Opmap = {
        '==': '=',
        '>=': '>=',
        '<=': '<=',
        '!=': '!=',
        '<': '<',
        '>': '>',
    }

    kif = "if"
    kelsif = "elsif"
    kelse = "else"
    kendif = "endif"

    tMSGCSTR = "MSGCSTR_"
    tSETFUNC = "SETFUNC_"
    tMODSTATEFUNC = "MODSTATEFUNC_"

    tCOND = "COND_"
    tNCOND = "NCOND_"
    tASSIGN = "ASSIGN_"
    tSEND = "SEND_"
    tMCAST = "MCAST_"
    tBCAST = "BCAST_"

    tnetworkready = "_network_ready()"

    ####################################################################################################################
    # GENERAL DEFERING
    vdeferpref = "defer_"

    # DEFER MESSAGE SEND HANDLING
    tGEN_BASE_MSG = "GEN_BASE_MSG_"
    tSEND_BASE_DEFER = "SEND_BASE_DEFER_"

    # LL DEFER MESSAGE
    iLL_Defer = "ll_defer"
    tPUSH_LL_DEFER = "PUSH_LL_DEFER_"
    tPOP_LL_DEFER = "POP_LL_DEFER_"

    # HL DEFER MESSAGE
    iHL_Defer = "hl_defer"
    tPUSH_HL_DEFER = "PUSH_HL_DEFER_"
    tPOP_HL_DEFER = "POP_HL_DEFER_"

    # NON-STALLING DEFER MESSAGE
    iStall_Defer = "stall_defer"
    tPUSH_STALL_DEFER = "PUSH_STALL_DEFER_"
    tPOP_STALL_DEFER = "POP_STALL_DEFER_"
