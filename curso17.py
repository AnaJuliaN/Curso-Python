#funções e escopos
#escopos de um nome é a parte de um código onde o nome é reconhecível corretamente
def my_function():
    var = 2
    print("Eu conheço aquela variável?", var)

var = 1
my_function()
print(var)

#palavra-chave global - usar ela dentro de uma função com o nome de uma variável, força o python a não criar uma nova variável dentro da função
def fun():
    global x
    x = 2
    print("Eu conheço aquela variável?")

x = 1
fun()
print(x)

#argumentos
def function(n):
    print("Eu obtive", n)
    n += 1
    print("Eu tenho", n)

y = 1
function(y)
print(y)

#----------------------------------
def my_f(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_f(my_list_2)
print("Print #5:", my_list_2)

#alterando-----------------------
def my_fun(list_1):
    print("Print #1:", list_1)
    print("Print #2:", list_2)
    del list_1[0]
    print("Print #3:", list_1)
    print("Print #4:", list_2)

list_2 = [2, 3]
my_fun(list_2)
print("Print #5:", list_2)