def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65))

#####################################

def imc(peso, altura):
    if altura < 1.0 or peso > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2

print(imc(352.5, 1.65))
#barra invertida usada para informar o Python para continuar a linha de código na prox linha de código

####################################

#convertendo unidades imperiais em unidades métricas
def lb_to_kg(lb):
    return lb * 0.45359237

print(lb_to_kg(1))

#-----------------------------------------
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(1, 1))

#######################################
#triângulos
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    
    return True
    
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

#triângulos e o teorema de pitágoras
def e_um_triangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input('Digite o primeiro lado\'s comprimento: '))
b = float(input('Digite o segundo lado\'s comprimento: '))
c = float(input('Digite o terceiro lado\'s comprimento: '))

if e_um_triangulo(a, b, c):
    print('Sim, pode ser um triângulo.')
else:
    print('Não, não pode ser um triângulo.')

###########################################################################
#Fatoriais
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6): #testando
    print(n, factorial_function(n))

###########################################################
#Fibonacci
def fib(f):
    if f < 1:
        return None
    if f < 3:
        return 1
    
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, f + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for f in range(1, 10):
    print(f, "->", fib(f))
