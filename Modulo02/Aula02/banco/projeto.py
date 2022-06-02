# Implementar a construção de uma classe chamada conta - ok
# Deverão ter outras classes herdando desta - ContaCorrente | ContaPoupança | ContaSalario - ok
# Deverão existir métodos e atributos capazes de permitir
# Sacar, ver saldo, depositar e transferir valores para as contas quando fizer sentido!
# As classes conta, contaCorrente, contaPoupança e contaSalario ***Deverão ser arquivos separados
# Analisar e implementar os métodos e atributos utilizando conceito de herança a fim de evitar reescrever código
# Também deverá existir um arquivo chamado projeto onde terá um menu permitindo utilizar os respectivos 
# métodos e atributos.
# Nesse menu, deverá existir uma opção para selecionar o tipo de conta (corrente|poupança|salário)
# Apenas encerrar o projeto com a opção SAIR selecionada.
# Reescrever código.
# Validar o numero da conta com 5 digitos existente na lista.
# Tempo estimado: 40 min


from Aula02.banco.funcoes import ExisteSaldo
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
from contaSalario import ContaSalario
import funcoes as f
import msgGerais as msg



contasC = {} # conta corrente
contasP = {} # conta poupanca
contasS = {} # conta salario

op = 0
tipoConta = 0

f.limpaTela()
while op != 5:
    print(' Banco Proway '.center(40,'='),
            '\n1 - Criar Conta\n'
            '2 - Listar Conta\n'
            '3 - Excluir Conta\n'
            '4 - Operações\n'
            '5 - Sair\n')

    op = int(input('Informe a opção desejada: ').center(40,' '))
    f.limpaTela()
    match op:
        case 1:
            tipoConta = f.validaTipoConta(True)
            f.limpaTela()
            numero = input('Informe o número da conta com 5 digítos: ')
            if (not f.EhContaValida(numero)):
                f.aguardaLimpa()
            
            else:
                match tipoConta:
                    case 1:
                        if (not (f.ExisteConta(numero,contasC))):
                            c = ContaCorrente(numero)
                            contasC[c.conta] = 0
                            print(msg.MSG_SUCESSO_CADASTRO)
                            del(c)

                    case 2:
                        if (not (f.ExisteConta(numero,contasC,True))):
                            c = ContaSalario(numero)
                            contasS[c.conta] = 0
                            print(msg.MSG_SUCESSO_CADASTRO)
                            del(c)

                    case outraOpcao:
                        if (not (f.ExisteConta(numero,contasC))):
                            c = ContaPoupanca(numero)
                            contasP[c.conta] = 0
                            print(msg.MSG_SUCESSO_CADASTRO)
                            del(c)
        case 2:
            tipoConta = f.validaTipoConta()
            f.limpaTela()
            match tipoConta:
                case 1:
                    if (f.ExisteContaCadastrada(contasC,tipoConta)):
                        print(contasC)
                case 2:
                    if (f.ExisteContaCadastrada(contasC,tipoConta)):
                        print(contasS)

                case 3:
                    if (f.ExisteContaCadastrada(contasC,tipoConta)):
                        print(contasP)
                case outraCaso:
                    print('Conta corrente')
                    print(contasC)
                    print('Conta salário')
                    print(contasS)
                    print('Conta poupança')
                    print(contasP)
            f.aguardaLimpa()

        case 3:
            tipoConta = f.validaTipoConta()
            f.limpaTela()
            match tipoConta:
                case 1:
                    if f.ExisteContaCadastrada(contasC,tipoConta):
                        numero = input(msg.MSG_CONTA_PARA_EXCLUIR)
                        if f.EhContaValida(numero):
                            if f.ExisteConta(numero, contasC):
                                c = ContaCorrente(numero)
                                contasC.pop(c.conta)
                                print(msg.MSG_SUCESSO_EXCLUIR)
                                del(c)
                case 2:
                    if f.ExisteContaCadastrada(contasS,tipoConta):
                        numero = input(msg.MSG_CONTA_PARA_EXCLUIR)
                        if f.EhContaValida(numero):
                            if f.ExisteConta(numero, contasS):
                                c = ContaSalario(numero)
                                contasS.pop(c.conta)
                                print(msg.MSG_SUCESSO_EXCLUIR)
                                del(c)
                case outraCaso:
                    if f.ExisteContaCadastrada(contasP,tipoConta):
                        numero = input(msg.MSG_CONTA_PARA_EXCLUIR)
                        if f.EhContaValida(numero):
                            if f.ExisteConta(numero, contasP):                           
                                c = ContaPoupanca(numero)
                                contasP.pop(c.conta)
                                print(msg.MSG_SUCESSO_EXCLUIR)
                                del(c)
                    f.aguardaLimpa()
        case 4:
            tipoConta = f.validaTipoConta()
            f.limpaTela()
            match tipoConta:
                case 1:# Conta corrente
                    op = f.menuOperacoes(tipoConta)
                    match op:
                        case 1:#Sacar
                            numero = int(input(msg.MSG_NUMERO_CONTA))
                            if f.ExisteConta(numero,contasC):
                                valor = int(input(msg.MSG_VALOR_SAQUE))
                                if f.ExisteSaldo(numero,contasC,tipoConta,valor):
                                    contasC[numero] -= (valor + (valor * 0.05))
                                    print(msg.MSG_SUCESSO_SAQUE)
                        case 2:#Deposito
                            numero = input(msg.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero): 
                                if f.ExisteConta(numero,contasC):
                                    valor = int(input(msg.MSG_VALOR_DEPOSITO))
                                    contasC[numero] += valor
                                    print(msg.MSG_SUCESSO_DEPOSITO)
                        case 3:#Transferência
                            numero = input(msg.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasC):
                                    numeroDest = input(msg.MSG_NUMERO_CONTA_DESTINO)
                                    tipoDestino = f.validaTipoConta()
                                    if f.ExisteConta(numeroDest,tipoDestino):
                                        valor = (msg.MSG_VALOR_TRANSFERENCIA)
                                        if f.ExisteSaldo(numero,contasC,tipoConta,valor):
                                            contasC[numero] -= valor

                                            match tipoDestino:
                                                case 1:
                                                    
                                                    if f.ExisteConta(numeroDest,contasC):
                                                        valor = int(input(msg.MSG_VALOR_TRANSFERENCIA))
                                                        if ExisteSaldo(numero,contasC,tipoConta,valor):
                                                            contasC[numero] -= valor
                                                            contasC[numeroDest] += valor
                                                case 2:
                                                    if f.ExisteConta(numeroDest,contasS):
                                                        valor = int(input(msg.MSG_VALOR_TRANSFERENCIA))
                                                        if f.ExisteSaldo(numero,contasC,tipoConta,valor):
                                                            contasC[numero] -= valor
                                                            contasS[numeroDest] += valor
                                                case outraCaso:
                                                    if f.ExisteConta(numeroDest,contasP):
                                                        valor = int(input(msg.MSG_VALOR_TRANSFERENCIA))
                                                        if f.ExisteSaldo(numero,contasC,tipoConta,valor):
                                                            contasC[numero] -= valor
                                                            contasP[numeroDest] += valor
                                                    
                                            f.limpaTela()
                                            print(msg.MSG_SUCESSO_TRANSFERENCIA)
                                            f.aguardaLimpa()
                

        case outraOpcao:# Conta poupança
            op = input(msg.MSG_NUMERO_CONTA)
            if f.EhContaValida(numero):
                if f.ExisteConta(numero,contasC):
                    match op:
                        case 1:#Sacar
                            valor = int(input(msg.MSG_VALOR_SAQUE))
                            
                        case 2:#Depositar
                            valor = int(input(msg.MSG_VALOR_DEPOSITO))
                            
                        case 3:
                            valor = int(input(msg.MSG_VALOR_TRANSFERENCIA))
                        case 4:
                            numero = input(msg.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasP):
                                    print(contasP[numero])
                        case outraCaso:
                            break

                    
        case 5:
            print(msg.MSG_ENCERRA_SISTEMA)
            f.aguardaLimpa()
            break
        case outraCaso:
            print(msg.MSG_OPCAO_INVALIDA)
            f.aguardaLimpa()
                    






