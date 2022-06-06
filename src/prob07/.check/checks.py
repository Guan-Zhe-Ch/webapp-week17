import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..', 'tools'))
from mylibs import chk_template
from random import randint

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"


def isPrime(v):
    if v<2: return False
    for n in range(2,int(v**0.5)+1):
        if v%n==0:
            return False
    return True

def expected():
    dat = [randint(1, 30) for _ in range(randint(10, 30))]
    idat = " ".join([str(_) for _ in dat])
    has3 = ",".join([str(_) for _ in filter(lambda x: '3' in str(x), dat)])
    prime = ",".join([str(_) for _ in filter(isPrime,dat)])
    gt10 = ",".join([str(_) for _ in filter(lambda x:x > 10, dat)])
    odat = f"get_gt10(data) => {gt10}\nget_has3(data) => {has3}\nget_prime(data) => {prime}"
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
    chk_template.main(root, 0, loops)
