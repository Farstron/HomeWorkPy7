import modul
import WR_phonebook as WRP

def find_information(inf):
    data = modul.data_store()
    result = []
    for i in data:
        temp = []
        for j in i:
            temp.append(i.get(j))
        if inf in ' '.join(temp):
            result.append(i)
    return result


def list_iformation(inf):
    inf = inf.split()
    data = modul.data_store()
    result = []
    for j in inf:  
        result.append(j)     
        for i in data:
            result.append(i.get(j))
        result.append('\n')
    return result

def reader():
    if modul.now_format() == 'txt':
        return WRP.read_txt()

# def transform():
