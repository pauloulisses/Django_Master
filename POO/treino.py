#PROPRIEDADES
class Notebook():
    marca = 'Dell'
    modelo = ' vostro'
    cor = 'cinza'

  # FUNÇÕES
    def acessar_internet(self):
      print('Acesar a Internet')

    def jogar(self):
      print('Jogar gamers')

    def programar(self):
      print('Programa')    


    def propriedades(self):
      print(f"Marca: {self.marca}")
      print(f"modelo:{self.modelo}")
      print(f"cor: {self.cor}")
    
 # INSTANCIA DE CLASSES
notebook = Notebook()   


# chamando o metodo para exibir a propriedade do notebook
notebook.propriedades()

#chamando outros metodos
notebook.acessar_internet()
notebook.jogar()
notebook.programar()


