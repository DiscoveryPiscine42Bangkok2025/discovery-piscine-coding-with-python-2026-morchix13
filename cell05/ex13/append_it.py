#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    printed = False
    for param in sys.argv[1:]:
        if not param.endswith("ism"):
            print(param + "ism")
            printed = True
    if not printed:
        pass
