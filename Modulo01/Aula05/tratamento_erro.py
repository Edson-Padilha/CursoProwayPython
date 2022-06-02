try:
    try:
        try:
            vl1 = int(input('Informe um valor inteiro: '))
            vl2 = int(input('Informe outro valor inteiro: '))
            print('O resultado da divisão dos valores é: ' + str(vl1 / vl2))
            print('Obrigado por usar nosso sistema!!!')

        except NameError:
                print('Alguma variável não existe')
        
        except ZeroDivisionError:
            print('Impossível dividir por zero.')
        except ValueError:
            print('Algum valor inválido foi passado.')
        except TypeError:
            print('Tipo de dado inválido.')
        except:
            print('Algo deu errado.')
    except:
        print('Erro ao informar o primeiro valor.')
except:
    print('Erro ao efetuar a divisão.')