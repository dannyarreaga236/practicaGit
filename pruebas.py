import ejercicio1 as ej1

# Probar la tabla
numero = int(input('Que tabla quieres? '))
ej1.tabla(numero)

# Probar el area del cuadrado
lado = int(input('Cuanto mide el lado? '))
ej1.area_cuadrado(lado)

# Probar las operaciones
op = int(input('1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\nElige una operacion: '))
num1 = int(input('Ingresa el primer numero: '))
num2 = int(input('Ingresa el segundo numero: '))
ej1.operacion(num1, num2, op)