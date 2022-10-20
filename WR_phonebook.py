import csv
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

def read_csv() -> list:
    res_data = []
    with open('phonebook.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for i in csv_reader:
            if i != []:
                temp = {}
                temp['Имя'] = i[0]
                temp['Фамилия'] = i[1]
                temp['Номер'] = i[2]
                temp['Город'] = i[3]
                res_data.append(temp)
    return res_data

def write_csv(res_data):
    print(res_data)
    with open('phonebook.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for i in res_data:
            csv_writer.writerow(i.values())