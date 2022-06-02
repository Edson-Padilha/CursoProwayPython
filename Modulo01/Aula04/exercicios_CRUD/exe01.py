# Você deverá implementar um sistema onde seja possível cadastrar, alterar,
# visualizar e excluir itens de uma lista de produtos de informática
# Deverá ter um menu com as opções para que o usuário informe a opção desejada
# Não poderá inserir itens duplicados
# Caso tente alterar, visualizar ou excluir item inesistente, o sistema deve informar
# isso para o usuário
# Ao alterar, deverá pedir qual item deseja alterar a para qual nome
# Caso o novo nome esteja já cadstrado, não permitir
# A cada iteração deverá limpar a tela e mostrar o menu novamente
# Devrá ser totalmente feito utilizando subrotinas
# Por questões de organização, as rotinas do CRUD deverão estar em um arquivo
# separado e especifico
# Tempo estimado: 35 minutos

import menu
while True:    
    menu.crud (x = int(input('Digite sua opção: ')))
    menu.time.sleep(2)   
    menu.menu()
