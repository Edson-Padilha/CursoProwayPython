lista = ['dois','quatro','seis','cinco']
print(lista)
# Adiona no final da lista
lista.append('tres')
print(lista)
# Adiciona por indice
lista.insert(0,'um')
print(lista)
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)
# Pop se não passar indice, remove o ultimo elemento
lista.pop(1)
print(lista)
# Remove elemento da lista por valor
lista.remove('dois')
print(lista)
# Alterar elemento
lista[1] = 'segundo'
print(lista)

for x in range(0,len(lista)):
    #print(lista[x])
    # Melhorando o print
    print(str(x+1) + 'º item => ' + lista[x])