
numero = int(input('Informe o número: '))

n1 = 0 
n2 = 1
n3 = 0
while n3 < numero:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
if(n3 == numero):
    print(f'O numero {numero} pretence a sequencia!')
else:
    print(f'O numero {numero} não pertence a sequência.')