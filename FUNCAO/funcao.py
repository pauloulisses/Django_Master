# enviando emails
def envia_email(nome, email):
    nome_dest = nome
    email_dest = email
    return f'Email enviado para {nome}, dona do email {email}'

pessoas = ['paulo', 'pauloulusses']
emails = ['pauloulisses1212@gmail.com', 'pauloulusses@gmail.com']

for pessoa, email in zip(pessoas, emails):
    email_enviado = envia_email(pessoa, email)
    print(email_enviado)

