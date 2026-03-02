#!/usr/bin/env python3

import os

from fairmd.lipids import FMDL_SIMU_PATH, FMDL_MOL_PATH
from fairmd.lipids.api import get_OP
from fairmd.lipids.core import initialize_databank
from fairmd.lipids.auxiliary import CompactJSONEncoder

from pprint import pprint
import json
import yaml


lname = "CHOL"
xchg = os.path.join(
    FMDL_MOL_PATH,
    "membrane",
    lname,
    "xchange.yaml"
)
with open(xchg, 'r') as fd:
    xc_dic = yaml.load(fd, Loader=yaml.SafeLoader)
pprint(xc_dic)

def apply_xchg(opdata, xc_dic):
    new_opdata = {}
    for k, v in opdata.items():
        new_k = xc_dic[k.split()[0]] + " " + xc_dic[k.split()[1]]
        new_opdata[new_k] = [v]
    return new_opdata

def change_simulations():
    ss = initialize_databank()
    for s in ss:
        if lname not in s.lipids:
            continue
        try:
            opdata = get_OP(s)[lname]
        except FileNotFoundError:
            # it sometimes happens..
            continue
        print(s)
        new_opdata = apply_xchg(opdata, xc_dic)

        opnm = os.path.join(
            FMDL_SIMU_PATH,
            s["path"],
            lname+"OrderParameters.json"
        )
        with open(opnm, 'w') as fd:
            json.dump(new_opdata, fd, cls=CompactJSONEncoder)



