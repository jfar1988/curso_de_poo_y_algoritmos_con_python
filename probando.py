class Carro:
    def __init__(self):
        pass
    def tipo_de_carro(self, combustible = 'gasolina'):
        self._marca(combustible)
        self._modelo()
        self._color()
        self._traccion()
        self._numero_de_puertas()

    def _marca(self, combustible):
        print(f'Renault a {combustible}')
    
    def _modelo(self):
        print('2012')
    
    def _color(self):
        print('Gris')
    
    def _traccion(self):
        print('Delantera')

    def _numero_de_puertas(self):
        print('Cuatro puertas')

if __name__ == '__main__':
    Carro = Carro()
    Carro.tipo_de_carro()




