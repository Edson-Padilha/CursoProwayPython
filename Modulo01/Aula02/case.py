op = int(input('Digite a opção desejada [1] [2] [3] [4]:'))
match op:
    case 1:
        print('Primeira opção')
    case 2:
        print('Segunda opção')
    case 3:
        print('Terceira opção')
    case 4:
        print('Quarta opção')
    case outraOpcao:
        print('Opção Inválida!')