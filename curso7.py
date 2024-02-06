#igualdade
var = 0
print(var == 0)

var = 1
print(var == 0)

#desigualdade
var = 0 
print(var != 0)

var = 1
print(var != 0)

#LAB
n = int(input("Digite um número: "))
print(n >= 100)

#if, else e elif - exemplo 1
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digiteo segundo número: "))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print("O maior número é:", larger_number)

#exemplo 2
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digiteo segundo número: "))

if number1 > number2: larger_number = number1
else: larger_number = number2

print("O maior número é:", larger_number)

#exemplo 3
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digiteo segundo número: "))
number3 = int(input("Digite o terceiro número: "))

largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

print("O maior número é:", largest_number)

#exemplo4
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digiteo segundo número: "))
number3 = int(input("Digite o terceiro número: "))

largest_number = max(number1, number2, number3)

print("O maior número é:", largest_number)

#LAB
name = input("Digite o nome da flor:")

if name == "Spathipyllum":
    print("Sim - Spathipylluum é a melhor planta de todos os tempos!")
elif name == "spathipyllum":
    print("Não, eu quero uma grande Spathipyllum!")
else:
    print("Spathipyllum! Não" + name + "!")

#LAB2
year = int(input("Digite um ano: "))

if year < 1582:
    print("Não dentro do período do calendário gregoriano")
else:
    if year % 4 != 0:
        print("ano comum")
    elif year % 100 != 0:
        print("Ano bissexto")
    elif year % 400 != 0:
        print("ano comum")
    else:
        print("Ano bissexto")