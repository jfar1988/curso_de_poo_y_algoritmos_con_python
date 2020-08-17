class   Coordenanda:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenanda):
        x_diff = (self.x - otra_coordenanda.x)**2
        y_diff = (self.y - otra_coordenanda.y)**2
        
        return (x_diff + y_diff)**0.5

if __name__ =='__main__':
    coord_1 = Coordenanda(3, 30)
    coord_2 = Coordenanda(4, 8)

    print(coord_1.distancia(coord_2))
    print(isinstance(3, Coordenanda))