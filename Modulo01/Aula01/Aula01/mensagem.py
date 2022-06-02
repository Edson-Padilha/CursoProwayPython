# Atribuindo valores de forma estática
linhas = ('=')*60
print(linhas)
msg = 'Hello Word! Seja bem vindo ao curso de Python!!!'
print(linhas)
print('O valor ', msg,' - O tipo de dados é: ',type(msg))
print(linhas)
msg = 2
print('O valor ', msg,' - O tipo de dados é: ',type(msg))
msg = 1.5
print('O valor ', msg,' - O tipo de dados é: ',type(msg))
msg = True
print('O valor ', msg,' - O tipo de dados é: ',type(msg))

# Atribuindo valores de forma dinâmica
print('Atribuindo valores de forma dinâmica')
print(linhas)
valor = input('Informe o valor que deseja para variável: ')
print(valor)
print(type(valor))

print(linhas)

inteiro = int(valor)
print(inteiro)
print(type(inteiro))
print(linhas)
del(valor)# Limpando a variavel da memória
#print(valor)
#print(type(valor))

valor = int(input('Digite um valor inteiro: '))
print(valor)
print(type(valor))