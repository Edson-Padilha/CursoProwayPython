from conta import Conta
import msgGerais as msg

class ContaPoupanca(Conta):
    def transferir(self,valor):
        try:
            if valor > self.saldo:
                return msg.MSG_SALDO_INSUFICIENTE
            self.saldo -= valor
            return msg.MSG_SUCESSO_TRANSFERENCIA
    
        except:
            return msg.MSG_ERRO_TRANSFERENCIA

    def depositar(self,valor):
        try:            
            self.saldo += valor
            return msg.MSG_SUCESSO_DEPOSITO

        except:
           return msg.MSG_ERRO_DEPOSITO