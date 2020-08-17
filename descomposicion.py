class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)
    
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self.motor.inyecta_gasolina(3)
        self._estado = 'en_movimiento'

    def traccion(self, autopista, destapado):
        self.autopista = '2x4'
        self.destapado = '4x4'
        print(destapado)

class Motor:
    def __init__(self, cilindros, tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass


