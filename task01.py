# Запуск поиска по заданным параметрам 
 
def find_with_parametrs(lf_str): 
    with open('save.txt','r',encoding = 'UTF-8') as save_info: 
        for line in save_info: 
            if  str(lf_str).lower() in str (line).lower(): 
                print(line) 
 
# запрос параметра поиска 
 
def ask_for_parametrs(): 
    print('Введите данные или оставьте поле пустым для вывода всех данных') 
    print('Поиск:') 
    lf_str = str(input()) 
    return lf_str            
 
# Заполнение данных 
 
def import_new_data(): 
    print('Введите новые данные в формате: Имя Фамилия Телефон ') 
    with open('save.txt','a',encoding = 'UTF-8') as save_info: 
        save_info.writelines(input())
        save_info.write('\n')
    print('Данные внесены')    
 
#import_new_data()
#find_with_parametrs(ask_for_parametrs())

# Изменение данных

def mod(info):
    with open('save.txt', 'a',encoding = 'UTF-8') as data: 
        list_rep = []
        for line in data:
            if info in line.split(): list_rep.append(input(f'{line} --> ').lower() + '\n')
            else: list_rep.append(line)
    with open('save.txt', 'w') as data:        
        data.writelines(list_rep)
    print('Данные изменены.')
    data.close()   

# Удаление данных 

def delete(info):
    with open('save.txt') as data:
        list_del = []
        for line in data:
            if info in line: print(f'Данные по {line} удалены')
            else: list_del.append(line)
    with open('save.txt','w') as data:
        data.writelines(list_del)
        data.close()          
  
    
