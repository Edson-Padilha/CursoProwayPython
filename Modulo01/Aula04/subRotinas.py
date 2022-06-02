# Função sempre retorna valor
# Procedimento só printa na tela
import os
import time

def mensagem(pValor):
    print(pValor)

def mensagem2():
    print('Seja bem vindo')

def somaValores(pValor1,pValor2):
    print('A soma dos valores é: '+ str(pValor1 + pValor2))
    

mensagem('Adoro programar em Python')
mensagem2()
somaValores(4,12)

def EhPar(pValor):
    if pValor % 2 == 0:
        return True
    return False

if EhPar(4):
    print('Valor é par')
else:
    print('Não é par')

