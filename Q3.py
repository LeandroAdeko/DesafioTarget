"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora de todos os dias de um ano, faça um programa, na linguagem que desejar, que calcule e retorne:

- O menor valor de faturamento ocorrido em um dia do ano;
- O maior valor de faturamento ocorrido em um dia do ano;
- Número de dias no ano em que o valor de faturamento diário foi superior à média anual.

a) Considerar o vetor já carregado com as informações de valor de faturamento.

b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média.

c) Utilize o algoritmo mais veloz que puder definir.
"""


def analise_faturamento(faturamento: list):

    # Remover dias sem faturamento
    faturamento = [f for f in faturamento if f > 0]

    media_faturamento = sum(faturamento) / len(faturamento)

    dias_acima_da_media = sum(1 for f in faturamento if f > media_faturamento)

    print(f"Menor faturamento: {min(faturamento)}")
    print(f"Maior faturamento: {max(faturamento)}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")


analise_faturamento([100, 200, 0, 50, 300, 0, 150, 0, 0, 500, 600, 0])