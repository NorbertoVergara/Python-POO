"""
capturar el nombre = str
capturar las ventas mensuales (12) =int
el usuario decide cuando terminar el bucle 
si no desea seguir mostrar el total deb mostar las ventas de registradad del programa
valor proct ventas y nombre
"""

class Vendedor:
    def __init__(self, nombre:str, ventas: list[float]) -> None:
        self.__nombre= nombre
        self.__ventas= ventas
    def getVentasDelUsuario(self):
        return self.__ventas
    def setVentas(self, indice:int , valor: float):
        self.__ventas[indice] = valor
    def setNombre(self, n):
        self.__nombre = n
    def getNombre(self):
        return self.__nombre
    def __str__(self) -> str:
        return f'{self.__ventas}'
    def totalVentas(self):
        return self.__ventas
    def totalVentasAnuales(self):
        return sum(self.__ventas)

vendedores = []
ventasTotales= []
ventasxvendedor= []
cont= 0
while True:    
    nombre = input('Ingrese el nombre del vendedor: ')
    
    ventas = [float(input(f'Ingrese la venta del mes {i+1}: ')) for i in range(2)] 
    ventasxvendedor.append(ventas)
    ventasTotales += ventas
    
    vendedor = Vendedor(nombre, ventas)
    vendedores.append(vendedor)
    
    pregunta= int(input("Menu: \n(1) Agregar un vendedor  \n(2) Modificar un vendedor \n(3) Cerrar programa \n: "))
    
    if pregunta == 1:
        print(vendedores[0].getNombre())
        continue
    elif pregunta == 2:
        validacion= int(input("Ingrese numero de posicion del vendedor que desee modificar:  \n " ))
    
    
    
    
    elif pregunta == 3:
        print(f"Las ventas totales fue: {sum(ventasTotales)}")
        break




for i in vendedores:
    print(i)
