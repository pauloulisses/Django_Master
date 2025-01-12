# POLIFORMISMO DE INTERFACE

# class base
class Forma():
    def area(self):
        pass

# class forma recebe os parametros da class formas
class Quadrado(Forma):

    def __init__(self, lado): # construtor da classe 
        self.lado = lado

    def area(self):
        return self.lado ** 2

quadrado = Quadrado(5)    
arae_quadrado = quadrado.area()
print(arae_quadrado)