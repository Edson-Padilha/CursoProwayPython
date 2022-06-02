# Elaborar um algoritimo que peca para o usuario ir digitando um valor inteiro
# A saída dolaco sera -1
# Ao final, devera retornar a soma dos valores informados

soma = 0
valor = 0

while (valor != -1):
    soma = soma + valor
    valor = int(input('Digite numero inteiro: '))
    print('Soma dos valores: ' + str(soma))