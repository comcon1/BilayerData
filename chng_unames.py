#!/usr/bin/env python3

import os

from fairmd.lipids import FMDL_SIMU_PATH, FMDL_MOL_PATH
from fairmd.lipids.core import initialize_databank
from fairmd.lipids.auxiliary import CompactJSONEncoder

from pprint import pprint
import yaml

ss = initialize_databank()

lname = "CHOL"

for s in ss:
    if "CHOL" in s.lipids:
        print(s)
    xchg = os.path.join(
        FMDL_MOL_PATH,
        "membrane",
        lname,
        "xchange.yaml"
    )
    with open(xchg, 'r') as fd:
        xc_dic = yaml.load_all(fd, Loader=yaml.SafeLoader)
    pprint(xc_dic)

    opnm = os.path.join(
        FMDL_SIMU_PATH,
        s["path"],
        lname+"OrderParameters.json"
    )


