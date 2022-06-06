import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..', 'tools'))
from mylibs import chk_template
from random import randint

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"



def expected():
    dat = [[t, randint(1,100)] for t in range(0,randint(15,50),5)]
    datx = [j for sub in dat for j in sub]
    idat = " ".join([str(_) for _ in datx])
    odat = "<table>\n  <tr>\n    <th>時間</th> <th>豆子溫度</th>\n  </tr>\n"
    for t1,t2 in dat:
        odat = odat + f"  <tr>\n    <td>{t1}</td> <td>{t2}</td>\n  </tr>\n"
    odat = odat + "</table>"
    print(f"Test Data : {idat}")
    return idat, odat


chk_template.expected = expected

if __name__ == "__main__":
    # print(f"cur = {sys.argv[0]}")
    root = sys.argv[0].replace(".check\checks.py", "")
    root = root.replace(".check/checks.py", "")
    loops = 10
    if len(sys.argv) == 2:
        loops = int(sys.argv[1])
    chk_template.main(root, 3, loops)
