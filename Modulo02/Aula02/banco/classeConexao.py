import mysql.connector

class Conexao():
    def __init__(self,host,banco,usuario,senha):
        self.host = host
        self.banco = banco
        self.usuario = usuario
        self.senha = senha
        
       

    def select(self,pTabela,pCampos,pClausula = [' ']):
        conn = mysql.connector.connect(host=self.host,user=self.usuario,database=self.banco,passwd=self.senha)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'SELECT ' 
            sqlc = ' '
            for i in range(0,len(pCampos)):
                sqlc += pCampos[i] + ' , '
            sqlc = sqlc[:-2]
            sql += sqlc + ' FROM ' + pTabela 
            sqlw = ''
            if pClausula[0] != ' ':
                for i in range (0,len(pClausula)):
                    if i == 0:
                        sqlw = ' WHERE ' + pClausula[i]
                    else:
                        sqlw += ' AND ' + pClausula[i]
                sql += sqlw + ';'
                #print(sql)
                #return
                
            cursor.execute(sql)
            total = 0
            for linha in cursor:
                total += 1
            
            if total < 1:
                print(pTabela +' Não possui registros... ')
            else:
                print('Registros da tabela '+ pTabela)
                cursor.execute(sql)
                for linha in cursor: 
                    print('Cod.: ' + str(linha))         
                    #print('Numero: ' + str(linha[0]))
                    #print('Saldo: ' + str(linha[2]))
                print('Total de registros: '+ str(cursor.rowcount))
            try:
                conn.is_connected()
                print('Conexão efetuada com sucesso!')
            except:
                print('Erro de conexão ao banco de dados...')

    def insert(self,pTabela,pCampos,pValores):
        conn = mysql.connector.connect(host=self.host,user=self.usuario,database=self.banco,passwd=self.senha)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'INSERT INTO ' + pTabela + '('
            sqlC = ' '
            for i in range(0,len(pCampos)):
                sqlC += pCampos[i] + ', '
            sqlC = sqlC[:-2] + ')'
            sql += sqlC + 'VALUES ('
            sqlV = ' '
            for i in range(0,len(pValores)):
                if type(pValores[i]) is str:
                    sqlV = '"' +  pValores[i] + '", '
                else:
                    sqlV += str(pValores[i]) + ', '
            sqlV = sqlV[:-2] + ')'
            sql += sqlV
            #print(sql)
            #return
            cursor.execute(sql)  
            try:
                conn.commit()
                print('Registro inserido com sucesso!')
            except:
                print('Erro ao inserir registro...')
        else:
            print('Não está conectado ao BD...')

    def delete(self,pTabelas,pClausula = [' ']):
        conn = mysql.connector.connect(host=self.host,user=self.usuario,database=self.banco,passwd=self.senha)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'DELETE FROM ' + pTabelas 
            sqlW = ' '
            if pClausula[0] != ' ':
                sqlW += 'WHERE '
                for i in range(0,len(pClausula)):
                    if i == 0:
                        sqlW = pClausula[i]
                    else:
                        sqlW += 'AND ' + pClausula[i]
            sqlW = sqlW
            sqlW += sqlW + '; '
            #print(sql)
            #return
            cursor.execute(sql)
            try:
                conn.commit()
                print('Registro excluído com sucesso!')
            except:
                print('Erro ao excluir o registro...')
        else:
            print('Não está conectado ao BD...')

    def update(self,pTabelas,pCampos,pValores,pClausula = [' ']):
        conn = mysql.connector.connect(host=self.host,user=self.usuario,database=self.banco,passwd=self.senha)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'UPDATE ' + pTabelas + ' SET '
            sqlC = ' '
            for i in range(0, len(pCampos)):
                if type(pValores[i]) is str:
                    sqlC += pCampos[i] + ' = ' + pValores[i] + ', '
                else:
                    sqlC = sqlC[:-2]
                    sqlW = ' '
            if pClausula[0] != ' ':
                sqlW = ' WHERE '
                for i in range(0,len(pClausula)):
                    if i == 0:
                        sqlW += pClausula[i]
                    else:
                        sqlW += ' AND ' + pClausula[i]
            sql += sqlC + sqlW + ';'
            #print(sql)
            #return
            #sql = 'UPDATE conta_corrente SET numero_conta_corrente = "00000" where id_conta_corrente = 10'
            cursor.execute(sql)
            try:
                conn.commit()
                print('Registro alterado com sucesso!')
            except:
                print('Erro ao atualizar registro...')
        else:
            print('Não está conectado ao BD...')

conexao = Conexao('localhost','banco','root','')

campos = ['numero_conta_corrente','saldo_conta_corrente']
valores = ['22222',90]
conexao.insert('conta_corrente',campos,valores)

campos = ['numero_conta_corrente','saldo_conta_corrente']
clausula = ['1=1','id_conta_corrente >= 2','numero_conta_corrente != " "']
conexao.select('conta_corrente ',campos)

campos = ['numero_conta_corrente','saldo_conta_corrente']
valores = ['98954',10.0]
conexao.insert('conta_corrente',campos,valores)

campos = [' * ']
conexao.select('conta_corrente ',campos)

campos = ['numero_conta_corrente','saldo_conta_corrente']
valores = ['99999',100]
clausula = ['numero_conta_corrente = "88888"']
conexao.update('conta_corrente',campos,valores,clausula)

campos = [' * ']
conexao.select('conta_corrente ',campos)

clausula = ['numero_conta_corrente = 98952']
conexao.delete('conta_corrente ',clausula)

campos = [' * ']
conexao.select('conta_corrente ',campos)

#conexao.select('conta_salario')
#conexao.select('conta_poupanca')
#conexao.insert('conta_corrente',campos,valores)
#conexao.delete('conta_corrente ',clausula)
#conexao.update('conta_corrente',campos,valores,clausula)