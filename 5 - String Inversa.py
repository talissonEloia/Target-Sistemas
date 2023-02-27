
# Define a string
string = input('Digite a string: ')

# Imprime a string invertida
print(string[::-1])


'''
#OUTRA FORMA

#converter string em lista de caracteres
list_char = list(string)

#inverter ordem dos caracteres
tamanho = len(list_char)

for i in range(tamanho//2):
    list_char[i], list_char[tamanho-i-1] = list_char[tamanho-i-1], list_char[i]

#converter lista em string novamente
str_inverse = ''.join(list_char)

#imprime a string invertida
print(str_inverse)

'''
