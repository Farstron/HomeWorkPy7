from controler import find_information as FIIN

def get_task(stop = False):
    global interfaceCommnds
    if stop != True:
        inf = input('Что вы хотите сделать?(для вывода возможных команд введите help)')
        if inf == 'help':
            help_list()
        if inf == 'стоп':
            print('Всего доброго!')
            return get_task(stop = True)
        if inf == 'получить данные':
            print(FIIN())
        return get_task()

def help_list():
    global interfaceCommnds
    for i in interfaceCommnds:
        print(i, '-',interfaceCommnds.get(i))

interfaceCommnds = {1:'help', 2:'получить данные', 3:'выдать список', 4:'перевести в другой формат', 5:'добавить данные',
0:'стоп'}
