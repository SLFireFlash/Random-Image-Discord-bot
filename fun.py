import json
from random import randint


def coolImoji():
    with open ("coolImoji.json",'r')as iF:
        idata =json.load(iF)
        num =str(randint(0,19))
    return idata[num]

