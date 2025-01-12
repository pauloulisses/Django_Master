class Animal:

    def emitir_som(self):
        print('Qualquer som...')

class Cachorro(Animal):
    def emitir_som(self):
        print('AU AU!')

class Gato(Animal):
    def emitir_som(self):
        print('MIUA!')             

cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()
