

def somaValores(obj):
    total = 0
    for cont in range(0,len(obj)):
        total += obj[cont]
    print (total)

def divideValores(obj):
    valor1 = 0
    valor2 = 0
    for cont in range(0,len(obj)):
        if cont == 0:
            valor1 = obj[cont]
        if cont == 1:
            valor2 = obj[cont]
            break
    try:
        print(valor1 / valor2)
    except ZeroDivisionError:
        print('Impossível dividir por zero')
    except:
        print('Ocorreu algum erro.')

def defineOpcao(obj, popcao):
    match popcao:
        case 1:
            somaValores(obj)
        case 2:
            divideValores(obj)
        case outroCaso:
            print ('Opção inválida.')
        
