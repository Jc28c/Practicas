numero_1 = input('Ingresa un numero primo: ')
numeros_ingresados = []
while not numero_1.isnumeric():
    numero_1 = input('Valor invalido, intente nuevamente: ')
    while numero_1.isnumeric():
        numeros_ingresados.append(numero_1)
        numero_1 = input('Valor aceptado, ingrese el siguiente numero o escriba stop para detener la solicitud de numeros: ')
    if str(numero_1) == 'stop':
        break    
print(numeros_ingresados)
