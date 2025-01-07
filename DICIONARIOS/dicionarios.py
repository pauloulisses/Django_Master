pessoa = {
    'nome': 'Eberson',
    'idade': '32',
    'profissão': 'dev',
    'interesses': ['python', 'programação', 'notebooks'],
    'pet': {
        'nome': 'Loki',
        'idade': '1',
        'peso': '2kg',
    }
}

# Buscando os itens da lista interesses
# Buscando o índice 1 da lista interesses
print(pessoa.get('interesses')[1])  # Saída: programação

# Acessando o nome do pet
print(pessoa.get('pet').get('nome'))  # Saída: Loki
print(pessoa['pet']['nome'])  # Outra forma de acessar o nome do pet. Saída: Loki

# Adicionando elemento dentro do dicionário
pessoa['Ano_nascimento'] = 1997
print(pessoa)  # Exibe o dicionário atualizado

# adicionando mais intens ao dicionários
pessoa['cores_favorita'] = 'azul, verde, rosa'
print(pessoa)

# Adicionando dicionário
pessoa['mae'] = {
    'nome': 'Maria',
    'idade': 50
}
print(pessoa)