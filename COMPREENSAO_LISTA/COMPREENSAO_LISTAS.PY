# lista contem elementos array

numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)  


# a forma patrica de fazer 

#1. expressão
#2. for
#3. item
# 4. in
# 5. lista 

# Parte 1: Dobrando os números
numeros2 = [1, 2, 3, 4, 5]
numeros_dobrados2 = [numero * 2 for numero in numeros2]
print(numeros_dobrados2)

# Parte 2: Convertendo os nomes para maiúsculas
nomes = ['ANA', 'Felipe', 'JOÃO', 'Arlindo', 'Carlos']
nomes_maisculos = [nome.upper() for nome in nomes]
print(nomes_maisculos)

# Parte 3: Filtrando palavras que começam com a letra 'A' e convertendo para maiúsculas
nomes_maisculos2 = [nome.upper() for nome in nomes if nome[0] == 'A']
print(nomes_maisculos2)

