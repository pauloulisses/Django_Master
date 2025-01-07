def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')


clientes = ['Ana', 'Jonas', 'Felipe', 'Claudio', 'Renato']

# Laços de repetição
# FOR - percorre a lista e atribui os intens da lista
# de clientes para a variável cliente
# o I representa o índice (começa em 0)
# break - interrompe o laço
for i, cliente in enumerate(clientes):
 if i == 2:
    break
 print( i, cliente)

 