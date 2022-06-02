import os
from time import sleep
import msgGerais as msg

def limpaTela():
    os.system('cls')

def aguarda():
    sleep(4)

def aguardaLimpa():
    aguarda()
    limpaTela()

def validaTipoConta(pEhCadastro = False):
    #tipoConta = 0

    tipoConta = int(input(msg.MSG_TIPO_CONTA))

    while (not tipoConta in [1,2,3,4]):
        print(msg.MSG_OPCAO_INVALIDA)
        aguardaLimpa()

        tipoConta = int(input('Informe o tipo de conta desejada\n'
                                '\n1 - Conta corrente\n' +
                                '2 - Conta salário\n'
                                '3 - Conta poupança\n'
                                '4 - Todas\n'))
    return tipoConta
def menuOperacoes(pTipoConta):# 1 corrente|2 salario|3 poupança
    aguardaLimpa()
    print('Operação desejada:\n ')
    match pTipoConta:
        case 1:
            
            opcao = int(input('1 - Sacar\n'
                              '2 - Depositar\n'
                              '3 - Transferir\n'
                              '4 - Ver saldo\n'
                              '5 - Encerrar\n'))
            
            while ( not (opcao in [1,2,3,4,5])):
                print(msg.MSG_OPCAO_INVALIDA)
                opcao = int(input('1 - Sacar\n'
                                  '2 - Depositar\n'
                                  '3 - Transferir\n'
                                  '4 - Ver saldo\n'
                                  '5 - Voltar\n'))
            return opcao   
                 
        case 2:
            opcao = int(input('1 - Sacar\n' 
                              '2  - Ver saldo\n'
                              '3 - Voltar'))

            while not (opcao in [1,2,3]):
                print(msg.MSG_OPCAO_INVALIDA)
                opcao = int(input('1 - Sacar\n' 
                                  '2 - Ver saldo\n'
                                  '3 - Voltar'))
            return opcao

        case 3:
            opcao = int(input('1 - Sacar\n' 
                              '2 - Depositar\n'
                              '3 - Transferir\n'
                              '4 - Ver saldo\n'
                              '5 - Voltar\n'))
            while not (opcao in [1,2,3,4,5]):
                opcao = int(input('1 - Sacar\n' 
                              '2 - Depositar\n'
                              '3 - Transferir\n'
                              '4 - Ver saldo\n'
                              '5 - Voltar\n'))
            return opcao             
            
        
def EhContaValida(pConta):
    if len(pConta) != 5:
        print(msg.MSG_NUMERO_CONTA_INVALIDO)
    return len(pConta) == 5

def ExisteConta(pNumero,pConta,pEhCadastro=False):
    if not pEhCadastro:
        if not pNumero in pConta:
            print(msg.MSG_CONTA_INEXISTENTE)
        return pNumero in pConta

def ExisteContaCadastrada(pConta,pTipoConta):
    if pConta == 0:
        if len(pTipoConta) == 1:
            print(msg.MSG_SEM_CONTA_CORRENTE)
        elif pTipoConta == 2:
            print(msg.MSG_SEM_CONTA_SALARIO)
        else:
            print(msg.MSG_SEM_CONTA_POUPANCA)

    return len(pConta) > 0

def ExisteSaldo(pNumero,pConta,pTipoConta,pValorOp):
    temSaldo = True
    if pTipoConta == 1:#Conta corrente
        if (pValorOp + (pValorOp * 0.05) > pConta[pNumero]):
            temSaldo = False
    if pTipoConta in [2,3]:#Demais contas
        if (pValorOp > pConta[pNumero]):
            temSaldo = False

    if (not (temSaldo)):
        print(msg.MSG_SALDO_INSUFICIENTE)
    return temSaldo
            