carros = []
carros.extend(['Marea', 'corsa'])  # Adiciona 'Marea' e 'corsa' como itens separados
print(carros)
# Saída: ['Marea', 'corsa']

# append ira incluir o item na ultima posição da lista
carros.append('Gol')
print(carros)


# adiconar elemento na posição que quiser
carros.insert(1, 'Fiat')
print(carros)

# Removendo o ultimo elemento da lista
carros.pop()
print(carros)

# removendo o elemento pelo idice

del carros[2]
print(carros)

# removendo o elemento especificado
carros.remove('Marea')
print(carros)

# Encontrar a quantidade de quantos elementos do mesmo tem na lista
carros.count('Fiat')
print(carros)

# inverte a ordem da lista
carros.reverse()
print(carros)

# Organizar os elementos da lista em ordem alfabetica e numerica
carros.sort()
print(carros)