def read_txt():
    res_data = []
    with open('phonebook.txt','r') as data:
        getInf=data.readlines()
        for i in getInf:
            temp = {}
            temp['Имя'] = i.split()[0]
            temp['Фамилия'] = i.split()[1]
            temp['Номер'] = i.split()[2]
            temp['Город'] = i.split()[3]
            res_data.append(temp)
    return res_data

def write_txt(res_data):
    output_data = []
    for i in res_data:
        temp = [0,0,0,0]
        temp[0] = i.get('Имя')
        temp[1] = i.get('Фамилия')
        temp[2] = i.get('Номер')
        temp[3] = i.get('Город')
        output_data.append(' '.join(temp))
    with open('phonebook.txt','w') as data:
        data.write('\n'.join(output_data))
