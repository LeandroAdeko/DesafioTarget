"""
2) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____
"""


def padrao_a(repeticoes = 10):
    valores = []
    for i in range(0, repeticoes):
        ultimo = 1 + i * 2
        valores.append(ultimo)
    print(valores)


def padrao_b(repeticoes = 10):
    valores = []
    for i in range(1, repeticoes+1):
        ultimo = 2 ** i
        valores.append(ultimo)

    print(valores)


def padrao_c(repeticoes = 10):
    valores = []
    for i in range(repeticoes):
        ultimo = i**2
        valores.append(ultimo)

    print(valores)


def padrao_d(repeticoes = 10):
    valores = []
    count = 0
    while count < repeticoes*2:
        count += 1
        if count % 2 == 1:
            continue
        ultimo = count ** 2
        valores.append(ultimo)


    print(valores)


def padrao_e(repeticoes = 10):
    a, b = 1, 1
    valores = [a, b]

    for i in range(repeticoes - 2):
        a, b = b, a + b
        valores.append(b)

    print(valores)


def padrao_f():
    print([2, 10, 12, 16, 17, 18, 19, 200, 201, 202])


padrao_a()
padrao_b()
padrao_c()
padrao_d()
padrao_e()
padrao_f()
