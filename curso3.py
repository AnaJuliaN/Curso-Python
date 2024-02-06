print("Exponenciação")
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print()

print("Multiplicação")
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
print()

print("Divisão")
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
print()

print("Divisão de número inteiro (divisão arredondada)")
print(6 // 3)  # O arredondamento sempre vai para o número inteiro menor.
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print(-6 // 4)  # O resultado é dois pares negativos. O resultado real (não arredondado) é -1.5 em ambos os casos. No entanto, os resultados são sujeitos
# a arredondamento. O arredondamento vai em direção ao valor inteiro menor, e o valor inteiro menor é -2.
print(6. // -4)
print()

print("Comparação de divisão")
print(6 // 4)
print(6. // 4)
print(6 / 4)
print(6. / 4)
print()

print("Restante (módulo)")
print(14 % 4)
# 14 // 4 dá 3 -> este é o quociente inteiro;
# 3 * 4 dá 12 -> como resultado da multiplicação de quociente e divisor
# 14 - 12 dá 2 -> este é o restante
print(12 % 4.5)
print()

print("Adição")
print(-4 + 4)
print(-4. + 8)
print()

print("O operador de subtração, os operadores unários e binários")
print(-4 - 4)
print(4. - 8)
print(-1.1)
print()

print("Operadores e suas ligações")
# A ligação do operador determina a ordem das computações executadas por alguns operadores com igual prioridade, colocados lado a lado em uma expressão
# A maioria dos operadores do Python tem ligação do lado esquerdo, o que significa que o cálculo da expressão é realizado da esquerda para a direita.
print(9 % 6 % 2)
# da esquerda para a direita: primeiro 9 % 6 dá 3, e então 3 % 2 dá 1;
# da direita para a esquerda: primeiro 6 % 2 dá 0 e depois 9 % 0 causa um erro fatal;

print(2 ** 2 ** 3)
# 2 ** 3 -> 8; 2 ** 8 -> 256
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))
