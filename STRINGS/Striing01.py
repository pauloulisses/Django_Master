# Stringo cadeia de carácteres

 # A   U  L  A       P  Y  C  O  D  E  B  R
 # 0   1  2   3   4  5  6  7  8  9 10 11 12 
#-13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

texto = 'AULA PYCODEBR'
print(texto)

# Buscando o indiice da string
texto2 = 'AULA PYCODEBR'
print(texto2[2])


# capturando um trecho da string positiivo
print(texto2[0:5])

# pegando trecho da striing negativo
print(texto2[-9:-2])

# pegando da popsição x até o final da string
print(texto2[5:])

# descobrindo o tamanho da string
print(len(texto2))

# buscando quantas recorrencia existe do caractere
print(texto2.count('A'))

# buscando quantas recorrencias tem da palavra
print(texto2.count('AULA'))

# buscando quantas letras tem em uma faixa do texto
# aqui está buscando quantas letras 'P' tem da posição 5 até a posição 11
print(texto2.count('P', 5, 11))


# Passa a posição onde começou o texto
print(texto2.find('PYCODEBR'))

# Todo o texto em maiiúsculo
print(texto2.upper())

# Todo o texto em minúsculo
print(texto2.lower())

# Cola a primeira letra do seu texto em maiúscula e o resto em minúsculo
print(texto2.capitalize())

# Coloca a primeira letra de cada palavra da sua string maiúscula 
print(texto2.title())

# Retorna uma liista com todas as palvaras que encontrou no texto e dividi por espaços
print(texto2.split())


# Junta a lista de palavras a função join
# Nas '' oque  colocar irá fiicar no meio das palavras
texto3 = "Exemplo de texto para ser dividido e juntado"
lista_de_palavras = texto3.split()
texto_juntado = '-'.join(lista_de_palavras)
print(lista_de_palavras)  # Imprime a lista de palavras separadas
print(texto_juntado)      # Imprime o texto sem espaços


# Tirando os espaços em branco no inicio e no final das strings
texto4_espaçados = '  AULA PYCODEBR  '
print(texto4_espaçados.strip())

# Tirando espçao da direita
texto_diireita = '  AULA PYCODEBR'
print(texto_diireita.rstrip())

# Removendo espaços da esquerda
texto_esquerda = 'AULA PYCODEBR   '
print(texto_esquerda.lstrip())