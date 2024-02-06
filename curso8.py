#WHILE
largest_number =  -999999999

number = int(input("Digite um número ou digite -1 para parar: "))

while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Digite um número ou digite -1 para parar: "))

print("O maior número é:", largest_number)

##WHILE2
odd_numbers = 0
even_numbers = 0

number = int(input("Digite um número ou digite 0 para parar: "))

while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Digite um número ou digite 0 para parar: "))

print("Números ìmpares contam:", odd_numbers)
print("Número pares contam:", even_numbers)

#USANDO COUNTER PARA SAIR DO LOOP
counter = 5
while counter != 0:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)

#FOR
for i in range (10):
    print("O valor de i é atualmente", i)

for i in range (2, 8):
    print("O valor de i é atualmente", i)

for i in range (2, 8, 3):
    print("O valor de i é atualmente", i)
#O primeiro argumento passado para a função range() nos diz qual é o número inicial da sequência.
#O segundo argumento diz à função onde parar a sequência.
#O terceiro argumento indica qual a etapa, que realmente significa a diferença entre cada número na sequência de números gerada pela função.

#Se o conjunto gerado pela função range() estiver vazio, o loop não execuatará seu corpo. ex:
for i in range(1, 1):
    print("O valor de i é atualmente", i)

###################################################
power = 1
for expo in range(16):
    print("2 à potência de", expo, "é", power)
    power *= 2

#break - exemplo
print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")

#continue - exemplo
print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.")
print("Fora do loop.")

################################################
#com break
largest_number = -999999999
counter = 0

while True:
    number = int(input("Digite um número ou digite -1 para terminar o programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("O maior número é", largest_number)
else:
    print("Você não inseriu nenhum número.")

################################################
#com continue
largest_number = -999999999
counter = 0

number = int(input("Digite um número ou digite -1 para terminar o programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1
    if number > largest_number:
        largest_number = number
        number = int(input("Digite um número ou digite -1 para terminar o programa: "))

if counter:
    print("O maior número é", largest_number)
else:
    print("Você não inseriu nenhum número.")

#o loop while e o ramo else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#o loop for e o ramo else
for i in range (5):
    print(i)
else:
    print("else:", i) 