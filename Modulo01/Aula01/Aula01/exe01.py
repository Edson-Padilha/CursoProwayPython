n1 = int(input('Digite primeiro número: '))
oper = int(input('Qual operação?\n 1 = *\n 2 = -\n 3 = +\n 4 = / \n'))
n2 = int(input('Segundo número: '))

print('=======Incio==========')

if (oper == 1):
    print('Multiplicação: '+ str(n1 * n2))
elif (oper == 2):
    print('Subtração: ' + str(n1 - n2))
elif (oper == 3):
    print('Soma: ' + str(n1 + n2))
elif (oper == 4):
    print('Divisão: ' + str(n1 / n2))
else:
    print('Operador incorreto')

print('=======Fim==========')