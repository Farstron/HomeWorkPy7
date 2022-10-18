def find_information():
    inf = input('По какому человеку вы хотите найти информацию?(если не знаете имя или фамилию чеолвека, можете ввести номер телефона)')
    path = input('Из какой телефонной книги вы хотите взять данные?')
    with open(path,'r') as data:
        getInf=data.readlines()
    res = [getInf[i] for i in range(0,len(getInf)) if inf in getInf[i]]
    print(res)

def list_iformation():
    inf = input('Список чего вы хотите получить?')
    