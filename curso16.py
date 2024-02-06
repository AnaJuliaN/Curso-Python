#return sem uma expressão
def happy_new_year(wishes = True):
    print("Três...")
    print("Dois...")
    print("Um...")
    if not wishes:
        return
    
    print("Feliz Ano Novo!")
    
happy_new_year()

#return com uma expressão
def boring_function():
    return 123

x = boring_function()

print("O retorno da função boring_function é:", x)

#none
value = None
if value is None:
    print("Desculpe, você não carrega nenhum valor")

####################################################

def strange_function(n):
    if(n % 2 == 0):
        return True
    
print(strange_function(2))
print(strange_function(1))

#listas e funções
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))

def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list
    
print(strange_list_fun(5))

#ano bissexto - lab
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
test_data = [1900, 2000, 2016, 2024]
test_results = [False, True, True, False]
    
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "-> ", end="")
    result = is_year_leap(yr)

    if result == test_results[i]:
        print("Ok")
    else:
        print("Fracassado")


