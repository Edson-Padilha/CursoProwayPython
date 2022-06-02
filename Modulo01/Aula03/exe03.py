t200 = 0
t100 = 0
t50 = 0
t20 = 0
t10 = 0
t5 = 0
t2 = 0
t1 = 0

valor = int(input('Valor a sacar R$ '))

while ( valor >= 200 ):
    t200 += 1
    valor -= 200
while ( valor >= 100 ):
    t100 += 1
    valor -= 100
while ( valor >= 50 ):
    t50 += 1
    valor -= 50
while ( valor >= 20 ):
    t20 += 1
    valor -= 20
while ( valor >= 10 ):
    t10 += 1
    valor -= 10
while ( valor >= 5 ):
    t5 += 1
    valor -= 5
while ( valor >= 2 ):
    t2 += 1
    valor -= 2
while ( valor >= 1 ):
    t1 += 1
    valor -= 1
print('TOTAL DE NOTAS'.center(40,'-'))
if t200 > 0:
    print('Total de notas de R$ 200: '+ str(t200))
if t100 > 0:
    print('Total de notas de R$ 100: '+ str(t100))
if t50 > 0:
    print('Total de notas de R$ 50: '+ str(t50))
if t20 > 0:
    print('Total de notas de R$ 20: '+ str(t20))
if t10 > 0:
    print('Total de notas de R$ 10: '+ str(t10))
if t5 > 0:
    print('Total de notas de R$ 5: '+ str(t5))
if t2 > 0:
    print('Total de notas de R$ 2: '+ str(t2))
if t1 > 0:
    print('Total de notas de R$ 1: '+ str(t1))



