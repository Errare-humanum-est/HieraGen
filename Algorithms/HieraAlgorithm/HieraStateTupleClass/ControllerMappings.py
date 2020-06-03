from typing import Dict, List
from Algorithms.General.GenStateSets import StateSets


def access_request_mapping(statesets: StateSets) -> Dict[str, List[str]]:
    ''' Get access mappings from cache controller '''
    access_map = {}
    stable_states = statesets.get_stable_states()

    if not stable_states:
        assert "No stable states found"
    else:
        for entry in (stable_states[0].get_access_str() + stable_states[0].get_evict_str()):
            access_map[entry] = []

    for state in stable_states:
        for transition in state.getaccessmiss() + state.getevictmiss():
            if transition.getoutmsgtypes() not in access_map[transition.getaccess()]:
                for msg in transition.getoutmsgtypes():
                    if msg not in access_map[transition.getaccess()]:
                        access_map[transition.getaccess()].append(msg)
    return access_map

def remote_messages(statesets: StateSets) -> List[str]:
    remote_msg_list = []
    for state in statesets.get_stable_states():
        for transition in state.getremotemiss():
            if transition.getinmsg() not in remote_msg_list:
                remote_msg_list.append(transition.getinmsg())

    return remote_msg_list

def access_remote_mapping(cc_statesets: StateSets, dir_statesets: StateSets):
    access_map = access_request_mapping(cc_statesets)
    remote_msg_list = remote_messages(cc_statesets)

    access_remote_map = {}
    for key in access_map.keys():
        access_remote_map[key] = []

    for state in dir_statesets.get_stable_states():
        for transition in state.getremote():
            for access in access_map:
                if transition.getinmsg() in access_map[access]:
                    for outmsg in transition.getoutmsgtypes():
                        if outmsg in remote_msg_list:
                            if outmsg not in access_remote_map[access]:
                                access_remote_map[access].append(outmsg)

    return access_remote_map
