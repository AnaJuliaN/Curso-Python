var = 1
account_balance= 1000.0
client_name = "Anne"
print(var, account_balance, client_name)
print(var)
print()

var = "3.8.5"
print("Versão Python: " + var)
print()

print("Atribuindo novos valores a uma variável já existente:")
var = 1
print(var)
var = var + 1
print(var)
print()

print("Solução de problemas matemáticos simples:")
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
print()

# tarefa
john = 3
mary = 5
adam = 6
print(john, mary, adam)
total_apples = john + mary + adam
print("Número total de maçãs: ", total_apples)
print()

# LAB
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "milhas é", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros é", round(kilometers_to_miles, 2), "milhas")
print()
#a função round() usada tem a função de arredondar o resultado de saída para o número de casas decimais especificadas entre parênteses e 
# retornar um float.

# LAB
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)