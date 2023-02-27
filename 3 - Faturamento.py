import xml.etree.ElementTree as et

#Carregando dados XML
arquivo = et.parse('C:/Users/Lenovo/Desktop/Data Science/Python/Target Sistemas/dados (2).xml')

faturamento = []

for row in arquivo.findall('row'):
    valor = float(row.find('valor').text)
    faturamento.append(valor)

#print(faturamento)

#calcula o menor e maior valor de faturamento
menor = min(faturamento)
maior = max(faturamento)


#calcular média mensal de faturamento
soma = 0
dias_com_fat = 0

for valor in faturamento:
    if valor > 0:
        soma += valor
        dias_com_fat +=1

media = soma/dias_com_fat


#calcular o numero de dias de faturamento superior a média
acima_med = 0
for valor in faturamento:
    if valor > media:
        acima_med += 1

#imprime resultados
print(f'Menor faturamento R$ {menor:.2f}')
print(f'Maior faturamento R$ {maior:.2f}')
print(f'{acima_med} dias com faturamento acima da média.')
print(f'Faturamento Médio do mês R$ {media:.2f}')
