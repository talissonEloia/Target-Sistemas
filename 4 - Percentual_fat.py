#dic com faturamento do estado
faturamento = {
    'SP':67836.43,
    'RJ':36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Out': 19849.53
}
#faturamento total
total = sum(faturamento.values())

#calcula o percentual de cada estado
percentuais = {}
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    percentuais[estado] = percentual

#imprime resultados
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')