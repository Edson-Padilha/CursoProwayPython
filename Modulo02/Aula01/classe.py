from time import sleep
from tqdm import tqdm
import os

class Veiculo:
    # Atributos de classe
    ano = 2022

# Atributos de Instância
    def __init__(self,ano,portas,cor,velMaxima):
        self.ano = ano
        self.portas = portas
        self.cor = cor
        self.velMaxima = velMaxima
        self.ligado = False
        self.totalMarchas = 5
        self.marcha = 0
        self.velocidade = 0
        self.mudaMarcha = False

    def ligar(self):
        if self.marcha == 0:
            if not (self.ligado) :
                self.ligado = True
                self.mudaMarcha = True
                return 'Carro Ligado'
            return 'Carro já está ligado'
        return 'O carro precisa estar no neutro para ligar...'

    def desligar(self):
        if self.marcha == 0:
            if(self.ligado):
                self.ligado = False
                self.mudaMarcha = False
                return 'Carro desligado'
            return 'O carro já está desligado'
        return 'O carro precisa estar no neutro para desligar...'

    def subirMarcha(self):
        if self.ligado:
            if self.marcha < self.totalMarchas:
                self.marcha += 1
                return 'Está na marcha '+ str(self.marcha)
            return 'Já está na marcha '+ str(self.marcha)
        return 'O carro precisa estar ligado para subir marcha!'

    def descerMarcha(self):
        if self.ligado:
            if self.marcha > -1:
                self.marcha -= 1
                if self.marcha == 1:
                    return 'O carro está na marcha ré!'
                return 'Está na marcha '+ str(self.marcha)
            return 'O carro está andando de ré...'
        return 'O carro precisa estar desligado para subir marcha!'

    def acelerar(self):
        if self.ligado:
            self.velocidade += 20
            sleep(1)
            if self.velocidade < 21:              
                print(self.subirMarcha())
                for i in tqdm(range(2)):
                    sleep(0.5)
                
            elif self.velocidade >= 40 and self.velocidade < 60 and self.marcha < 2:
                print(self.subirMarcha())
                for i in tqdm(range(4)):
                    sleep(1)
            elif self.velocidade >= 60 and self.velocidade < 80 and self.marcha < 2:
                print(self.subirMarcha())
                for i in tqdm(range(6)):
                    sleep(0.9)
                    
            elif self.velocidade >= 80 and self.velocidade < 100 and self.marcha < 4:
                print(self.subirMarcha())
                for i in tqdm(range(8)):
                    sleep(0.8)
                    
            elif self.velocidade >= 100 and self.velocidade < 120 and self.marcha < 4:
                print(self.subirMarcha())
                for i in tqdm(range(10)):
                    sleep(0.7)
                    
            elif self.velocidade < self.velMaxima and self.velocidade >= 140 and self.marcha < 5:
                print(self.subirMarcha())
                for i in tqdm(range(12)):
                    sleep(0.6)
            return 'Velocidade atual: ' + str(self.velocidade)
        return 'O carro precisa estar ligado para acelerar!'

    


        
        
    
