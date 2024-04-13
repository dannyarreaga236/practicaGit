def tabla(numero):
    for x in range(1, 11):
        print(f"{numero} X {x} = {numero*x}")

def area_cuadrado(lado):
    print(f"El area es: {lado*lado}")

def operacion(num1, num2, op):
    match op:
        case 1:
            print(f'La suma es: {num1+num2}')
        case 2:
            print(f'La resta es: {num1-num2}')
        case 3:
            print(f'La multiplicacion es: {num1*num2}')
        case 4:
            print(f'La division es: {num1/num2}')
        case _:
            print('Opción inválida.')