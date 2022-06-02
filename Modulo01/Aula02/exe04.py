# Elabore um algoritimo que peça para o usuario informar u valor inteiro e imprima a tabuada.
# Ex: Informe um valor 3
# Tabuada de 3
# 3 x 1 = 3
# 3 x 2 = 6


print('========TABUADA==========')
tab = int(input('Digita a tabuada que deseja ver: '))

for i in range(tab,11):
    print('\nTabuada de '+ str(i))
    for cont in range(1,11):
        print(str(i) + ' x ' + str(cont)+' = ' + str(i * cont) )
    print('\n')


# Agora o cliente precisa de uma alteração.
# O usuário deverá informar um valor de 1 até para a tabuada.
# O sistema deverá trazer a tabuada do valor 
# 