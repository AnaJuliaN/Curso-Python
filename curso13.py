#lista de compreensão - exemplos
squares = [x ** 2 for x in range(10)]
print(squares)

twos = [2 ** i for i in range(8)]
print(twos)

odds = [x for x in squares if x % 2 != 0]
print(odds)

#natureza multidimensional das listas: aplicações avançadas
temps = [[0.0 for h in range(24)] for d in range(31)] #h - hora d - dia

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Temperatura média ao meio-dia:", average)

######################################################

temps = [[0.0 for h in range(24)] for d in range(31)]

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("A maior temperatura foi:", highest)

#######################################################

temps = [[0.0 for h in range(24)] for d in range(31)]

hot_days= 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "dias estavam quentes.")