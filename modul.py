from re import I
from typing import Counter
import WR_phonebook as WRP
from user_interface import now_path as NPA
from controler import reader
def data_store():
    global counter
    if counter == 0:
        counter += 1
        return reader()

def now_format():
    res = ''
    for i in reversed(NPA):
        if i != '.':
            res+=i 
        else: break
    return res

counter = 0