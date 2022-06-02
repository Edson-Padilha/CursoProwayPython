# Para ingressar no Exército Brasileiro como soldado, a pessoa deverá ter 18 anos
# Ser do sexo Masculino
#
#
#
nome = input('Digite seu nome: ').upper()
sexo = int(input('Escolha uma opção para sexo:\n'+
'1 = [ M ]\n'+
'2 = [ F ]\n'))

match sexo:
    case 1:
        idade = int(input('Digite sua idade: '))
        match idade:
            case 18:
                print(nome + ', você foi convocado para o serviço militar.')        
    case outraOpcao:
        print(nome + ', você foi dispensado do serviço militar.')

   