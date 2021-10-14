class MyDemo():
    nombre = ''
    def __init__(self, nombre):
        self.nombre = nombre
        pass

    def saludar(self):
        print(f'hola {self.nombre}')