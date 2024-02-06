print("Conte-me qualquer coisa...")
anything = input()
print("Hum...", anything, "...Realmente?")
print()

anything = input("Conte-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")

#A função input() - operações proibidas
anything = input("Digite um número: ")
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

#Resolvendo o problema das operações proibidas com conversão de tipo
anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)
print()

leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é", (leg_a**2 + leg_b**2) ** .5)

#Dando outra função para + e *
#Concatenação
fnam = input("Posso ter seu primeiro nome, por favor? ")
lnam = input("Posso ter seu sobrenomem, por favor? ")
print("Obrigado!")
print("\nSeu nome é " + fnam + " " + lnam + ".")

#Replicação
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
#Este programa "desenha" um retângulo

#Função str() - converter um número em uma string
leg_x = float(input("Insira o comprimento da primeira perna: "))
leg_y = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é" + str((leg_x**2 + leg_y**2) ** .5))
#Graças a função str(), podemos passar o resultado inteiro para a função print() como uma string, esquecendo as vírgulas

