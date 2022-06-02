try:
    arq = open('arquivo.txt','r')
    arq.close()
    print('O arquivo foi aberto para leitura e está fechado.')
except FileNotFoundError:
    print('O arquivo não existe e será criado.')
    arq = open('arquivo.txt','w')
    arq.write('Olá Mundo!!!')
    arq.close()
except:
    print('O arquivo existe, mas não pode ser aberto.')

try:
    arq = open('arquivo.txt')
    print('Seja bem vindo a manipulação de texto.')
    arq.close()
except:
    print('Ocorreu algum erro ao escrever o arquivo.')
try:
    arq = open('arquivo.txt','r')
    conteudo = arq.read()
    print(conteudo)
    arq.close()
except:
    print('Erro ao abrir arquivo para leitura.')