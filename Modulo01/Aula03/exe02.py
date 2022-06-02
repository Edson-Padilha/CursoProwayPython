# A Proway criou uma fintech para um banco. 
# Você foi contratado para desenvolver esse sistema. 
# Deverá ser informado login e senha para acessar. 
# considerar login - aluno | senha - proway
# após isso, deverá gerar um menu com as seguintes opções
# [Depositar | Sacar | Ver Saldo | Transferir | Sair]
# Apenas poderá sacar e transferir se existir saldo suficiente
# Para depositar, deverá pedir a conta de destino com 5 digitos.
# Tempo estimado: 20 min. 


login = input('Informe o login: ') #Login correto deve ser aluno
senha = input('Informe a senha: ') #Senha correta deve ser proway
while ( (login != 'aluno') or (senha != 'proway') ):
    print('Login/Senha inválidos')
    login = input('Informe o login: ')
    senha = input('Informe a senha: ')

op = 1
saldo = 0
while ( op > 0 ):
    print('BANCO PROWAY'.center(40,'-'))
    print('|1- Sacar '.ljust(20,' ') + '2- Depositar '.ljust(20,' ') + '|')
    print('|3- Transferir '.ljust(20,' ') + '4- Ver Saldo '.ljust(20,' ') + '|')
    print('|' + '5- Sair'.center(39) + '|')
    print(''.center(40,'-'))
    op = int(input('Operação desejada: '))
    match op:
        case 1:
            valor = int(input('Valor para saque: '))
            if ( valor > saldo ):
                print('Saldo insuficiente!')
            else:
                saldo -= valor
                print('Saque efetuado com sucesso')
        case 2:
            valor = int(input('Valor para depósito: '))
            saldo += valor
        case 3:
            valor = int(input('Valor para transferência: '))
            if ( valor > saldo ):
                print('Saldo insuficiente!')
            else:
                conta = input('Conta para transferência')
                if ( len(conta) == 5 ):
                    saldo -= valor 
                    print('Transferência efetuada com sucesso!')
                else:
                    print('Conta inválida')
        case 4:
            print('Saldo atual R$ ' + str(saldo))
        case 5:
            print('Sair')
            break
        case outrocaso:
            print('Opção inválida')