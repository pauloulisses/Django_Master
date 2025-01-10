class Celular:
    # PROPRIEDADES
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'

    # FUNÇÕES
    def fazer_ligações(self):
        print('Fazer ligação...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha...')

    def despertador(self):
        print('Despertando...')

    def calcular(self, v1, v2):
        return v1 + v2
            

    def exibir_propriedades(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Tem câmera: {self.tem_camera}")
        print(f"Bateria: {self.bateria}")


# INSTÂNCIA DE CLASSE
celular = Celular()

# Chamando o método para exibir propriedades
celular.exibir_propriedades()

# Chamando outros métodos
celular.fazer_ligações()
celular.jogar_cobrinha()
celular.despertador()
calculado = celular.calcular(2, 4)
print(calculado)

