# Dia 3
edad = 18
altura = 1.78
numeroComplejo = 18 + 4j

# area de un triangulo
seMultiplica = 0.5
alturaTriangulo = int(input("ingresa la altura del triangulo: "))
baseTriangulo = int(input("ingresa la base del triangulo: "))
areaDelTriangulo = seMultiplica * baseTriangulo * alturaTriangulo
print ("el area del triangulo es de: ", areaDelTriangulo)

# Perimetro del triangulo
primerLado = int(input("ingrese el primer lado del triangulo: "))
segundoLado = int(input("ingrese el segundo lado del triangulo: "))
tercerLado = int(input("ingrese el tercer lado del triangulo: "))
perimetroDelTriangulo = primerLado + segundoLado + tercerLado
print ("el perimetro del triangulo es de: ", perimetroDelTriangulo)

# Area y perimetro de un rectangulo
longitudRectangulo = int(input("ingrese la longitud del rectangulo: "))
anchuraRectangulo = int( input("ingrese la anchura del rectangulo: "))
areaDelRectangulo = longitudRectangulo * anchuraRectangulo
perimetroDelRectangulo = longitudRectangulo + anchuraRectangulo
print ("el area del rectangulo es de: ", areaDelRectangulo)
print ("el perimetro del rectangulo es de: ", perimetroDelRectangulo)

# Area del circulo
radio = int(input("ingrese el radio del circulo: "))
print (type(radio))
pi = 3.1416
areaOfCircle = pi * radio **2
circumOfCircle = 2 * pi * radio
print ('el area del circulo es: ', areaOfCircle)
print ('la circuferencia del circulos es: ', circumOfCircle)

# Pendiente, intersección con el eje x e intersección con el eje y de y = 2x - 2
pendiente = 2
interseccion_y = -2
# Para la intersección con el eje x
interseccion_x = -interseccion_y / pendiente
print("La pendiente es:", pendiente)
print("La intersección con el eje y es:", interseccion_y)
print("La intersección con el eje x es:", interseccion_x)

import math
# Coordenadas de los puntos
x1, y1 = 2, 2
x2, y2 = 6, 10
# Calcular la pendiente
pendiente = (y2 - y1) / (x2 - x1)
# Calcular la distancia euclidiana
distancia_euclidiana = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("La pendiente es:", pendiente)
print("La distancia euclidiana es:", distancia_euclidiana)








