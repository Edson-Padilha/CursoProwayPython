import time
produtos = []
x = 0 # Variavel utilizada no case

def menu():
    print(' SMJ SISTEMAS '.center(40,'-'))
    print('|'+('Escolha uma opção'.center(38,' ')+('|')))
    print('|'+(' 1 - Cadastrar Item'.ljust(38,' ')+('|')))
    print('|'+(' 2 - Excluir Item'.ljust(38,' ')+('|')))
    print('|'+(' 3 - Atualizar Item'.ljust(38,' ')+('|')))
    print('|'+(' 4 - Visualizar Item'.ljust(38,' ')+('|')))
    print('|'+(' 9 - Para Sair'.center(38,' ')+('|')))
    print('-'.ljust(40,'-'))    

def crud(x):    
    match x:
        
        case 9:
            print('Você saiu do sistema...')

        case 1:
            
            item = input('Nome do produto: ').strip().capitalize()
            if item in produtos:
                print('Produto já cadastrado...')
            else:
                produtos.append(item)
                print('Produto cadastrado com sucesso...')

        case 2:
            
            if len(produtos) == 0:
                print('Sua lista está vazia...')
                
            else:
                print('\n'+' Produtos cadastradados\n')

                for itens in range(0,len(produtos)):                    
                    print(str(itens + 1) + ' - ' + produtos[itens])
                item = input('Qual produto deseja excluir: ').strip().capitalize() 
            
                if item in produtos:       
                    produtos.remove(item)
                    print('Produto excluído com sucesso...')
                else:
                    print('Produto incorreto...')
        case 3:
            if len(produtos) == 0:
                print('Você não tem produtos cadastrados...')
            else:
                for itens in range(0,len(produtos)):
                    print(str(itens + 1) + ' - ' + produtos[itens])
                itens = int(input('Digite o código do produto: '))

                if itens <= len(produtos):
                    produtos[itens - 1] = input('Novo nome: ').strip().capitalize()

                    for itens in range(0,len(produtos)):
                        print(str(itens + 1) + ' - ' + produtos[itens])
                else:
                    print('Código inválido...')
                      
                       
        case 4:
            if len(produtos) == 0:
                print('Você não tem produtos cadastrados...')
            else:
                print('\n'+'RELATÓRIO DE PRODUTOS CADASTRADOS'.center(40,' ')+'\nCód. ' + ' Produto')

                for itens in range(0,len(produtos)):
                    print(str(itens + 1) + ' - ' + produtos[itens])
            print(' FIM '.center(40,'='))
                
         
menu()
crud(x)


