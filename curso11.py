#ordenando uma lista
my_list= [8, 10, 6, 2, 4] #lista para ordenar

for i in range(len(my_list)): #precisamos de (5 - 1) comparações
    if my_list[i] > my_list[i + 1]: #comparar elementos adjacentes
        my_list[i], my_list[i + 1] = my_list[i + 1],my_list[i] #se acabarmos aqui, nós temos que trocar os elementos.

#############################################

my_list = [8, 10, 6, 2, 4] #lista para ordenar
swapped = True #é um pouco falso, precisamos dele para entrar no loop while.

while swapped:
    swapped = False #nenhuma troca até agora.
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True #uma troca foi realizada
            my_list[i], my_list[i + 1] = my_list[i + 1],my_list[i]

print(my_list)

#A ordenação por bolhas - versão interativa
my_list = []
swapped = True
num = int(input("Quantos elementos você deseja embaralhar? "))

for i in range(num):
    val = float(input("Entre com a lista de elementos:"))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\n Sorted:")
print(my_list)

######################################################

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

#método reverse()
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst) #outputs: [4, 2, 1, 3, 5]