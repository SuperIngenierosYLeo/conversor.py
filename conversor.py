import pyfiglet
sistemaDeEntrada = ""
sistemaDeSalida = ""
valorAConvertir = ""
valorTransformado = 0
#Las siguientes definiciones son para los numeros validos de cada sistema inicial
sisBin = "01"
sisDec = "0123456789"
sisOctal = "01234567"
sisHexad = "0123456789ABCDEF"
print(pyfiglet.figlet_format("CONVERSOR DE BASES"))
#La variable juansito es para repetir la iteracion del programa hasta que el usuario lo requiera
juansito = 0
while juansito == 0:
    #El siguiente bucle while sirve para validar el ingreso del sistema numerico inicial segun correspoonda
    while True:
        tocayex=0
        sistemaDeEntrada=input("Seleccione el sistema del valor ingresado: \n 1. Binario\n 2. Decimal\n 3. Octal\n 4. Hexadecimal\n")
        if sistemaDeEntrada.isnumeric():
            sistemaDeEntrada=int(sistemaDeEntrada)
            if sistemaDeEntrada>0 and sistemaDeEntrada<5:
                tocayex+=1
            else:
                tocayex=0
            if tocayex!=0:
                break
            else:
                print("Elija una opcion valida para convertir")
            
        else:
            print("Ingrese el numero de segun el sistema que requiere")
            continue
    #El siguiente bucle funciona para validar el ingreso de un dato segun sea el sistema numerico inicial
    while True:
        i = 0    
        tocayex=0
        valorAConvertir=input("Ingrese el valor que desea convertir: \n")
        if sistemaDeEntrada==4:
            valorAConvertir=str(valorAConvertir)

        if sistemaDeEntrada==1:
            for i in range(len(valorAConvertir)):
                if valorAConvertir[i] not in sisBin:
                    tocayex=0
                    break
                else:
                    tocayex+=1
            if tocayex!=0:
                valorAConvertir = int(valorAConvertir)
                break
            else:
                print("El numero ingresado no es valido con sistema inicial, reingrese un nuevo numero")
        if sistemaDeEntrada==2:
            for i in range(len(valorAConvertir)):
                if valorAConvertir[i] not in sisDec:
                    tocayex=0
                    break
                else:
                    tocayex+=1
            if tocayex!=0:
                valorAConvertir = int(valorAConvertir)
                break
            else:
                print("El numero ingresado no es valido con sistema inicial, reingrese un nuevo numero")
        if sistemaDeEntrada==3:
            for i in range(len(valorAConvertir)):
                if valorAConvertir[i] not in sisOctal:
                    tocayex=0
                    break
                else:
                    tocayex+=1
            if tocayex!=0:
                valorAConvertir = int(valorAConvertir)
                break
            else:
                print("El numero ingresado no es valido con sistema inicial, reingrese un nuevo numero")
        if sistemaDeEntrada==4:
            for i in range(len(valorAConvertir)):
                if valorAConvertir[i] not in sisHexad:
                    tocayex=0
                    break
                else:
                    tocayex+=1
            if tocayex!=0:
                valorAConvertir = str(valorAConvertir)
                valorAConvertir=valorAConvertir.upper()
                break
            else:
                print("El numero ingresado no es valido con sistema inicial, reingrese un nuevo numero")
            
    #Este bloque realiza la validacion de elegir un sistema destino diferente al original
    while True:
        tocayex=0
        sistemaDeSalida = input("A que sistema desea convertir el numero: \n 1. Binario\n 2. Decimal\n 3. Octal\n 4. Hexadecimal\n")
        if sistemaDeSalida.isnumeric():
            sistemaDeSalida=int(sistemaDeSalida)
            if sistemaDeSalida>0 and sistemaDeSalida<5 and sistemaDeEntrada!=sistemaDeSalida:
                tocayex+=1
            else:
                print("Elija un sistema de salida valido")
                tocayex=0
            if tocayex!=0:
                break

    #El siguiente bloque realizara las operaciones para convertir entre sistemas
    while True:
        if sistemaDeEntrada==1:#BINARIO
            if sistemaDeSalida==2:#BINARIO DECIMAL
                decimal=0
                potencia=1
                while valorAConvertir > 0:
                    digito= valorAConvertir % 10  # Obtener el último dígito del número binario
                    decimal += digito * potencia  # Convertir y sumar al resultado decimal
                    potencia *= 2  # Actualizar la potencia de 2
                    valorAConvertir //= 10  # Eliminar el último dígito binario
                print("El numero transformado a decimal es: ",decimal)
                break
            if sistemaDeSalida==3:#BINARIOOCTAL
                # Paso 1: Convertir binario a decimal
                decimal = 0  # Resultado en decimal
                potencia = 1  # Representa 2^0
                while valorAConvertir > 0:
                    digito = valorAConvertir % 10  # Obtener el último dígito del número binario
                    decimal += digito * potencia  # Sumar el valor del dígito multiplicado por la potencia de 2 correspondiente
                    potencia *= 2  # Multiplicar potencia de 2 por 2 para el siguiente dígito
                    valorAConvertir //= 10  # Eliminar el último dígito binario
                # Paso 2: Convertir decimal a octal
                octal = ""  # Resultado en octal
                if decimal == 0:
                    octal = "0"  # Si el número decimal es 0, el resultado en octal es "0"
                while decimal > 0:
                    resto = decimal % 8  # Obtener el resto de la división por 8
                    octal = str(resto) + octal  # Añadir el dígito octal al inicio de la cadena
                    decimal //= 8  # Dividir el número decimal por 8
                # Asignar el resultado a valorTransformado
                valorTransformado = octal
                print("El numero transformado a octal es: ",valorTransformado)
                break
            if sistemaDeSalida==4:#BINARIO HEXADEC
                decimal = 0  # Inicializar decimal en 0
                potencia = 1

                while valorAConvertir > 0:
                    digito = valorAConvertir % 10  # Obtener el último dígito del número binario
                    decimal += digito * potencia  # Convertir y sumar al resultado decimal
                    potencia *= 2  # Actualizar la potencia de 2
                    valorAConvertir //= 10  # Eliminar el último dígito binario

                # Paso 2: Convertir decimal a hexadecimal
                hex_chars = "0123456789ABCDEF"  # Caracteres hexadecimales
                hexadecimal = ""  # Inicializar hexadecimal en una cadena vacía

                while decimal > 0:
                    resto = decimal % 16  # Obtener el resto de la división por 16
                    hexadecimal = hex_chars[resto] + hexadecimal  # Añadir el carácter hexadecimal al inicio
                    decimal //= 16  # Dividir el número decimal por 16

                # Si hexadecimal está vacío, significa que el número binario era 0
                if not hexadecimal:
                    hexadecimal = "0"

                # Asignar el resultado a valorTransformado
                valorTransformado = hexadecimal
                print("El numero transformado a hexadecimal es: ",valorTransformado)
            break
        #El siguiente condicional se aplica para realizar operaciones de Decimal a los otros sistemas
        if sistemaDeEntrada==2: #Decimal A Binario
            if sistemaDeSalida==1:
                binario = ""
                if valorAConvertir == 0:
                    binario = "0"
                while valorAConvertir > 0:
                    resto = valorAConvertir % 2  # Obtener el resto de la división por 2
                    binario = str(resto) + binario  # Añadir el resto al principio de la cadena binaria
                    valorAConvertir //= 2  # Dividir el número decimal por 2
                print("El numero convertido de decimal a binario es: ",binario)
                break
            if sistemaDeSalida==3:#decimal a octal
                octal = ""
                if valorAConvertir == 0:
                    octal = "0"
                while valorAConvertir > 0:
                    resto = valorAConvertir % 8  # Obtener el resto de la división por 8
                    octal = str(resto) + octal  # Añadir el resto al principio de la cadena octal
                    valorAConvertir //= 8  # Dividir el número decimal por 8
                print("El numero convertido de decimal a octal es: ",octal)
                break
            if sistemaDeSalida==4:#Decimal a Hexadecimal
                hex_chars = "0123456789ABCDEF"  # Caracteres hexadecimales
                hexadecimal = ""
                if valorAConvertir == 0:
                    hexadecimal = "0"
                while valorAConvertir > 0:
                    resto = valorAConvertir % 16  # Obtener el resto de la división por 16
                    hexadecimal = hex_chars[resto] + hexadecimal  # Añadir el carácter hexadecimal al principio de la cadena
                    valorAConvertir //= 16  # Dividir el número decimal por 16
                print("El numero convertido de decimal a hexadecimal es: ",hexadecimal)
                break
        if sistemaDeEntrada==3:#DesdeOctal
            if sistemaDeSalida==1: #Octal a Binario
                binario = ""
                # Paso 1: Convertir octal a decimal
                decimal = 0
                potencia = 1
                while valorAConvertir > 0:
                    digito = valorAConvertir % 10  # Obtener el último dígito del número octal
                    decimal += digito * potencia  # Convertir y sumar al resultado decimal
                    potencia *= 8  # Actualizar la potencia de 8
                    valorAConvertir //= 10  # Eliminar el último dígito octal
                # Paso 2: Convertir decimal a binario
                valorAConvertir = decimal
                if decimal == 0:
                    binario = "0"
                while valorAConvertir > 0:
                    resto = valorAConvertir % 2  # Obtener el resto de la división por 2
                    binario = str(resto) + binario  # Añadir el resto al principio de la cadena binaria
                    valorAConvertir //= 2  # Dividir el número decimal por 2
                print("El numero convertido de octal a binario es: ",binario)
                break
            if sistemaDeSalida==2:#Octal a decimal
                decimal = 0
                potencia = 1  # Empezamos con la menor potencia de 8 (8^0)
                while valorAConvertir > 0:
                    digito = valorAConvertir % 10  # Obtener el último dígito del número octal
                    decimal += digito * potencia  # Convertir el dígito octal a decimal y sumarlo
                    potencia *= 8  # Actualizar la potencia de 8 para el siguiente dígito
                    valorAConvertir //= 10  # Eliminar el último dígito octal
                print("El numero convertido de octal a decimal es: ",decimal)
                break
            if sistemaDeSalida==4:#Octal a Hexadecimal
                decimal = 0
                potencia = 1  # Empezamos con la menor potencia de 8 (8^0)
                while valorAConvertir > 0:
                    digito = valorAConvertir % 10  # Obtener el último dígito del número octal
                    decimal += digito * potencia  # Convertir el dígito octal a decimal y sumarlo
                    potencia *= 8  # Actualizar la potencia de 8 para el siguiente dígito
                    valorAConvertir //= 10  # Eliminar el último dígito octal
                # Paso 2: Convertir decimal a hexadecimal
                valorAConvertir = decimal
                hex_chars = "0123456789ABCDEF"  # Caracteres hexadecimales
                hexadecimal = ""
                if decimal == 0:
                    hexadecimal = "0"
                while valorAConvertir > 0:
                    resto = valorAConvertir % 16  # Obtener el resto de la división por 16
                    hexadecimal = hex_chars[resto] + hexadecimal  # Añadir el carácter hexadecimal al principio de la cadena
                    valorAConvertir //= 16  # Dividir el número decimal por 16
                print("El numero convertido de octal a hexadecimal es: ",hexadecimal)
                break
        if sistemaDeEntrada==4:#Desde hexadecimal
            if sistemaDeSalida==1:#Hexadecimal a Binario
                hex_to_bin = {
                    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
                    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
                }
                # Convertir hexadecimal a binario
                binario = ""
                for digito in valorAConvertir:
                    binario += hex_to_bin[digito]  # Concatenar la representación binaria del dígito hexadecimal
                print("El numero convertido de hexadecimal a binario es: ",binario)
                break
            if sistemaDeSalida==2:#Hexadecimal a decimal
                hex_to_dec = {
                    '0': 0, '1': 1, '2': 2, '3': 3,
                    '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'A': 10, 'B': 11,
                    'C': 12, 'D': 13, 'E': 14, 'F': 15
                }
                # Convertir hexadecimal a decimal
                decimal = 0
                potencia = 1  # Potencia inicial de 16 (16^0)
                # Recorrer el hexadecimal de derecha a izquierda
                for digito in reversed(valorAConvertir):
                    decimal += hex_to_dec[digito] * potencia  # Convertir y sumar al resultado decimal
                    potencia *= 16  # Actualizar la potencia de 16
                print("El numero convertido de hexadecimal a decimal es: ",decimal)
                break
            if sistemaDeSalida==3:#Hexadecimal a Octal
                hex_to_dec = {
                    '0': 0, '1': 1, '2': 2, '3': 3,
                    '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'A': 10, 'B': 11,
                    'C': 12, 'D': 13, 'E': 14, 'F': 15
                }
                decimal = 0
                potencia = 1  # Potencia inicial de 16 (16^0)
                # Recorrer el hexadecimal de derecha a izquierda
                for digito in reversed(valorAConvertir):
                    decimal += hex_to_dec[digito] * potencia  # Convertir y sumar al resultado decimal
                    potencia *= 16  # Actualizar la potencia de 16
                # Paso 2: Convertir decimal a octal
                valorAConvertir = decimal
                octal = ""
                if decimal == 0:
                    octal = "0"
                while valorAConvertir > 0:
                    resto = valorAConvertir % 8  # Obtener el resto de la división por 8
                    octal = str(resto) + octal  # Añadir el resto al principio de la cadena octal
                    valorAConvertir //= 8  # Dividir el número decimal por 8
                print("El numero convertido de hexadecimal a octal es: ",octal)
            break
    juansito=input("Desea realizar otro calculo?: 0.Si 2.No")
    if juansito.isnumeric():
        juansito=int(juansito)
        if juansito==0:
            continue
        else:
            break