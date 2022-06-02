# O código de trânsito brasileiro (CTB) prevê que, para conduzir veiculos automotores a pessoa precisa 
# Ter idade minima de 18 anos.
# Elabore um algoritimo que peça o nome e em que ano a pessoa nasceu,  e retorne se está pode
# ou não dirigir.
# Não totalmente satisfeito com o sistema e precisando de mais informações 
# o cliente precisa saber agora, quando não puder dirigir, quantos anos ele precisa esperar para poder dirigir.

print('==========PERMISSÃO PARA DIRIGIR==============')
nome = input('Informe seu nome: ').upper()
ano = int(input('Em que ano nasceu? '))
atual = 2022
resultado = atual - ano


if resultado <= 17:
    print(nome +', você não pode dirigir. Aguarde, '+ str(resultado) + ' anos')
elif resultado >= 80:
    print('Já ultrapassou seu tempo de dirigir!')
else:
    print(nome +', você pode dirigir.')