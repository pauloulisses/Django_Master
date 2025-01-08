import api
import os
# sistema operacional busque pra mim do ambiente o valor do meu usuario e senha
usuario = os.environ.get('USUARIO_API')
senha = os.environ.get('SENHA_API')

login = api.login(usuario, senha)
print(login)