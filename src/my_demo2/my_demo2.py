class MyDemo2():
    nombre = ''
    def __init__(self, nombre):
        self.nombre = nombre
        pass

    def despedir(self):
        print(f'Adios {self.nombre}')