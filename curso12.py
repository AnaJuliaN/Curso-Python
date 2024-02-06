list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

#fatia - é um elemento da sintaxe Python que permite fazer uma cópia totalmente nova de uma lista ou de partes de uma lista.
#ele copia o conteúdo da lista, não nome da lista.
list_1 = [1]
list_2 = list_1[:] #capaz de produzir uma nova lista, uma das formas mais gerais da lista: my_list[start:end]
list_1[0] = 2
print(list_2)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
#a lista new_list terá elementos end - start (3 - 1 = 2) - aqueles com índices iguais a 1 e 2 (mas não 3)
#start é ó índice do primeiro elemento incluido na fatia;
#end é o índice do primeiro elemento NÃO incluido na fatia.

#fatias - índices negativos
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1] #se o start especificar um elemento além do descrito no end (do início da lista), a fatia estará vazia
print(new_list) #output []

#se você omitir o start na fatia, presume-se que você deseja obter uma fatia começando no elemento com índice 0
#my_list[:end] equivalente a my_list[0:end]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list) #output [10, 8, 6]

#se você omitir o end da fatia, pressupõe-se que você deseja que a fatia termine no elemento com o índice len(my_list)
#my_list[start:] equivalente a my_list[start:Len(my_list)]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list) #output [4, 2]

#del também pode excluir fatias
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) #output [10, 4, 2]

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list) #exclui todos os elementos
#a instrução del sozinha excluirá a lista em si, não seu conteúdo como se estivesse numa fatia

#in - verifica se determinado elemento está atualmente armazenado em algum lugar dentro da lista
#not in - verifica se determinado elemento está ausente em uma lista
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#listas - alguns problemas simples
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

###########################################

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list

for i in my_list:
    if i > largest:
        largest = i

print(largest)

###########################################

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] ==  to_find
    if found:
        break

if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")