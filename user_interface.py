from controler import find_information as FIIN
from controler import list_iformation as LIIF
from controler import transform as TR
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
            con=input('Введите данны человека, чтобы получить полную информацию о нем:')
            print(*FIIN(con))
        
        if inf == 'выдать список':
            con = input('Список по какому критерию вы хотите получить?')
            print(' '.join(LIIF(con)))

        if inf == 'перевести в другой формат':
            TR()
            print('Перевод выполнен успешно!')
        return get_task()

def help_list():
    global interfaceCommnds
    for i in interfaceCommnds:
        print(i, '-',interfaceCommnds.get(i))

interfaceCommnds = {1:'help', 2:'получить данные', 3:'выдать список', 4:'перевести в другой формат', 5:'добавить данные',
0:'стоп'}

def now_path():
    NP = input('Введите название телефонной книги:')
    return NP