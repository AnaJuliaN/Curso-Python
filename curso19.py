#Tuplas
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

####################################
tupla = (1, 10, 100)

t1 = tupla + (1000, 10000)
t2 = tupla * 3

print(len(t2))
print(t1)
print(t2)
print(10 in tupla)
print(-10 not in tupla)

######################################
#Dicionário
dictionary = {
                "gato": "chat", 
                "cachorro": "chien", 
                "cavalo": "cheval"
            }
words = ['gato', 'lion', 'cavalo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "não está no dicionário")

print(dictionary['gato'])
#print(phone_numbers['Suzy'])

print()
######################################
#Métodos e funções
#keys()
dictionary1 = {
                "gato": "chat", 
                "cachorro": "chien", 
                "cavalo": "cheval"
            }

for key in dictionary1.keys():
    print(key, "->", dictionary1[key])


print()

#items()
dictionary2 = {
                "gato": "chat", 
                "cachorro": "chien", 
                "cavalo": "cheval"
            }

for english, french in dictionary2.items():
    print(english, "->", french)

print()

####################################
#modificação de valores
dictionary3 = {
                "gato": "chat", 
                "cachorro": "chien", 
                "cavalo": "cheval"
            }

dictionary3['gato'] = 'minou'
print(dictionary3)

#função sorted()

for key in sorted(dictionary3.keys()):
    print()

#adicionando uma nova chave
dictionary3['swan'] = 'cygne' #tbm aceita o método update
print(dictionary3)