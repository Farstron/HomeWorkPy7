import user_interface
import modul
import WR_phonebook as WRP

def find_information(inf, form):
    data = modul.data_store(form)
    result = []
    for i in data:
        temp = []
        for j in i:
            temp.append(i.get(j))
        if inf in ' '.join(temp):
            result.append(i)
    return result


def list_iformation(inf, form):
    inf = inf.split()
    data = modul.data_store(form)
    result = []
    for j in inf:  
        result.append(j)     
        for i in data:
            result.append(i.get(j))
        result.append('\n')
    return result

def reader(form):
    li = 0
    if form == 'txt':
        li = WRP.read_txt()
    else:
        li = WRP.read_csv()
    return li

def transform(form):
    if form == 'txt':
        WRP.write_csv(modul.data_store(form))
    else: WRP.write_txt(modul.data_store(form))