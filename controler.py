import modul

def find_information():
    inf = input('По какому человеку вы хотите найти информацию?(если не знаете имя или фамилию чеолвека, можете ввести номер телефона)')
    data = modul.data_store()
    result = []
    for i in data:
        temp = []
        temp.append(i.values())
        print(temp)
        if inf in ' '.join(temp):
            result.append(i)
    return result


def list_iformation():
    inf = input('Список чего вы хотите получить?')
    data = modul.data_store()
    result = []
    for i in data:
        temp = []
        temp.append(i.values())
        print(temp)
        if inf in ' '.join(temp):
            result.append(i)
    