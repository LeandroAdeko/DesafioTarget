"""
5) Dois veículos, um carro e um caminhão, saem respectivamente de cidades opostas pela mesma rodovia. O carro, de Ribeirão Preto em direção a Barretos, 
a uma velocidade constante de 90 km/h, e o caminhão, de Barretos em direção a Ribeirão Preto, a uma velocidade constante de 80 km/h. 
Quando eles se cruzarem no percurso, qual estará mais próximo da cidade de Ribeirão Preto?

a) Considerar a distância de 125km entre a cidade de Ribeirão Preto <-> Barretos.
b) Considerar 3 pedágios como obstáculo e que o carro leva 5 minutos a mais para passar em cada um deles, pois ele não possui dispositivo de cobrança de pedágio.
c)Explique como chegou no resultado.
"""


"""
Assumindo que os pedágios estão dividios de forma igual pelo trajeto teríamos a seguinte configuração

Ribeirão Preto - Carro |____[1]____[2]____[3]____| Caminhão - Barretos

A distancia entre os pedágios é de 31,25km 

p_distancia = 31.25

segundo_pedagio = {
    "carro": p_distancia*2 / 90 + (5 / 60)*2,
    "caminhao": p_distancia*2 / 80
}

print(f"
Até chegar ao segundo pedágio o caminhão precisa de {segundo_pedagio['caminhao']*60:.0f} minutos
Até chegar ao segundo pedágio o carro precisa de {segundo_pedagio['carro']*60:.0f} minutos

Quando o caminhão chegar ao pedágio terá percorrido {}
")

"""


print("""
Cai feito pato nessa.
Se eles se cruzaram eles estão no mesmo ponto, ou seja, na mesma distancia de Ribeirão Preto.
""")