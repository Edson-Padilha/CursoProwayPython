# Elabore um programa para manipular informações em uma lista.
# Os itens da lista deverão ser arquivos de informação.
# A cada operação executada (leitura, inserção, exclusão e edição da lista deverá gravar um log)
# O arquivo será 'log.txt'
# Implementar a função grava log e demais funções em arquivo separado.
# A função grava log deverá receber uma mensagem de parâmetro que será gravada.
# Tempo estimado: 20 minutos.

op = 0
x = 0
def menu():
    print(' SMJ SISTEMAS '.center(40,'-'))
    print('|'+('Escolha uma opção'.center(38,' ')+('|')))
    print('|'+(' 1 - Leitura'.ljust(38,' ')+('|')))
    print('|'+(' 2 - Inserção'.ljust(38,' ')+('|')))
    print('|'+(' 3 - Exclusão'.ljust(38,' ')+('|')))
    print('|'+(' 4 - Editar'.ljust(38,' ')+('|')))
    print('|'+(' 9 - Para Sair'.center(38,' ')+('|')))
    print('-'.ljust(40,'-')) 


def inserir(obj,valor):
    obj.append(valor)
    return valor + 'Cadastrado com sucesso"""'




def opcoes(x):
    
    match x:
        case 1:
            print('O arquivo está pronto para leitura')
            arq = open('texte.txt','r')
            arq.close()
        case 2:
            print('O arquivo teste.txt será criado.')
            arq = open('teste.txt','w')
            arq.close()
            
        case 3:
            pass
        case 4:
            print('Arquivo pronto para edição')
            arq = open('teste.txt','a')
            arq.close()
        case 9:
            print('Você saiu do sistema')
            
        
        


menu()
opcoes(x)