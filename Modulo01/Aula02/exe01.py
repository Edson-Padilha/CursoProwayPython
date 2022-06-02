# Elabore uma calculadora onde o usuário informa 2 valores inteiros
# Deverá selecionar a operação desejada [+ - x /] e retornar o resultado de acordo com a opção
# UTILIZAR CASE
# --------------------------

print('----------Calculadora-----------')

n1 = int(input('Digite primeiro numero: '))
n2 = int(input('Segundo numero: '))

op = int(input("Qual operação?\n"+
"1 = [ + ]\n"+
"2 = [ - ]\n"+
"3 = [ * ]\n"+
"4 = [ / ]\n"))

print('------RESULTADO--------')
match op:
    
    case 1:
        print('A soma é: '+ str( n1 + n2))
    case 2:
        print('A subtração é: '+ str(n1 - n2))
    case 3:
        print('A multiplicação é: '+ str(n1 * n2))
    case 4:
        if (n2 == 0):
            print('Impossível dividir por zero.')
        else:
            print('A divisão é: '+ str(n1 / n2))
    case erro:
        print('Opção inválida.')

print('=========Fim===========')
