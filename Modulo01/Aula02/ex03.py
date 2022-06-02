# VOCÊ FOI CONTRATADO PARA EFETUAR UM SISTEMA PARA UM POSTO DE COMBUSTÍVEIS
# PARA TANTO, DEVERÁ PEDIR O NOME DO MOTORISTA, 
# TAMBÉM DEVERÁ INFORMAR O COMBUSTÍVEL DESEJADO 
# [ETANOL, GASOLINA ADITIVADA, GASOLINA COMUM, DIESEL] COM OS RESPECTIVOS VALORES
# [4.689, 5.899, 7.099, 4.599]
# O SISTEMA DEVERÁ PERGUNTAR SE O MOTORISTA DESEJA INFORMAR O VALOR A PAGAR OU A QUANTIDADE DE LITROS
# CASO OPTE POR INFORMAR O VALOR, DEVERÁ PERGUNTAR QUANTO DESEJA PAGAR E RETORNAR OS LITROS ABASTECIDOS
# CASO OPTE POR INFORMAR OS LITROS, DEVERÁ PERGUNTAR QUANTOS LITROS E RETORNAR O VALOR A PAGAR

gasolina = 7.099
gasolinaAditivada = 5.899
diesel = 4.599
etanol = 4.689
print('========= Sistema de Posto de Combustível ========')
nome = input('Nome do motorista: ').upper()
tipo = int(input('Escolha a opção:\n'+
'1 = Litros\n'+
'2 = Valor Moeda\n'))

comb = int(input('Qual o combustivel: \n'+
'1 = Gasolina comum\n'+
'2 = Gasolina aditivada\n'+
'3 = Etanol\n'+
'4 = Diesel\n'))

match tipo:
    case 1:
        valor = int(input(nome + ', quantos litros: '))
        match comb:
            case 1:
                print('Valor a pagar R$ '+ str(valor * gasolina)) 
            case 2:
                print('Valor a pagar R$ '+ str(valor * gasolinaAditivada))
            case 3:
                print('Valor a pagar R$ '+ str(valor * etanol))
            case 4:
                print('Valor a pagar R$ '+ str(valor * diesel))
            case opcaoInvalida:
                print('Opção Inválida.')
match tipo:
    case 2:
        valor = int(input(nome +', valor R$ '))
        match comb:
            case 1:
                print('Litros abastecido: '+ str(valor / gasolina)) 
            case 2:
                print('Litros abastecido: '+ str(valor / gasolinaAditivada))
            case 3:
                print('Litros abastecido: '+ str(valor / etanol))
            case 4:
                print('Litros abastecido: '+ str(valor / diesel))
            case opcaoInvalida:
                print('Opção Inválida.')
    
