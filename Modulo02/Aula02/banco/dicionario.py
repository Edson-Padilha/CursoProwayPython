emails = {}

#print(type(d))

# Adicionando itens ao dicionario

emails['Juca'] = 'juca@hotmail.com'
emails['Edson'] = 'edsonp.bsi@gmail.com'
emails['Maria'] = 'maria@yahoo.com.br'
emails['Jucas'] = 'juca@ibest.com.br'
emails['lista'] = [1,2,3,4,5]

print(emails)

for x in emails:
    if emails[x][:3] == 'Juca':
        print(emails[x])

# Atualializando e-mail

if 'Juca' in emails:
    print('Existe')
    emails['Juca'] = 'emailAtualizado@gmail.com'

else:
    print('Não existe')
    emails['Juca'] = 'novoemail@hotmail.com'

# Remover um item de e-mail
try:
    emails.pop('Juca')
except:
    print('E-mail excluido com sucesso')

print(emails)