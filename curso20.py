#try:
    #esse é um lugar
    #que você pode fazer algo
    #sem pedir permissão
#except:
    #esse lugar é dedicado
    #apenas para implorar por perdão

try:
    value = int(input('Insira um número natural:'))
    print('O reciproco de', value, 'é', 1 / value)
except:
    print('Não sei o que fazer.')

#Duas excessões após um try
try:
    value = int(input('Insira um número natural:'))
    print('O reciproco de', value, 'é', 1 / value)
except ValueError:
    print('Não sei o que fazer.')
except ZeroDivisionError:
    print('A divisão por zero não é permitida em nosso universo.')

#A excessão padrão e como usá-la
try:
    value = int(input('Insira um número natural:'))
    print('O reciproco de', value, 'é', 1 / value)
except ValueError:
    print('Não sei o que fazer.')
except ZeroDivisionError:
    print('A divisão por zero não é permitida em nosso universo.')
except:
    print('algo de estranho aconteceu aqui... Desculpe!')