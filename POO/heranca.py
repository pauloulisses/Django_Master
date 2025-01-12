class Carro:
    # PROPRIEDADES
    numero_rodas = 4
    quantidade_passageiros = 5

    # FUNÇÕES
    def acelerar(self):
        print('Acelerando...')

    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Buzinar...')  


class Uno(Carro):
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992

class Gol(Carro):
    modelo = 'T-cros'
    marca = 'Volkswagen'   
    ano = 2023 
     

# INSTÂNCIA DA CLASSE UNO
print(Uno.modelo)
print(Uno.marca)
print(Uno.ano)

Uno.acelerar(Carro)


# INSTÂNCIA DA CLASSE Gol
print(Gol.modelo)
print(Gol.marca)
print(Gol.ano)

Gol.buzinar(Carro)