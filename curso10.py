numbers = [10, 5, 7, 2, 1]
print("Conteúdos originais da lista:",numbers)

numbers[0] = 111
print("Novo conteúdo da lista:", numbers)

numbers[1] = numbers[4]
print("Novo conteúdo da lista:", numbers)
print(numbers[0])
print("\n List lenght:", len (numbers))

#removendo elementos de uma lista
del numbers[1]
print(len(numbers))
print(numbers)

#índices negativos
numbers = [111, 7, 2, 1]
print(numbers[-1]) #pega o último da lista
print(numbers[-2]) #pega o penúltimo da lista

#função
#result = function(arg)
#uma função não pertence a nenhum dado - ela obtém dados, pode criar novos dados e (geralmente) produz um resultado

#método
#result = data.method(arg)
#um método faz tudo isso, mas também é capaz de alterar o estado de uma entidade selecionada

#append
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
numbers.append(4) #pega o valor do argumento e o coloca no final da lista que possui o método
print(len(numbers))
print(numbers)

#insert
numbers.insert(0, 222) #adiciona um novo elemento em qualquer lugar na lista, não apenas no final 
print(len(numbers))
print(numbers)

##############################################

my_list = [] #criando uma lista vazia

for i in range(5):
    my_list.append(i + i)

print(my_list)

##############################################

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
#calcula a soma de todos os valores armazenados na lista