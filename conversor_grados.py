import math

'''
1   Convertir grados Celsius a grados Fahrenheit

parametros de entrada: Parámetro tipo float con Valor en grados Celsius
aplicar formula: (valor en celcius * 9 / 5 + 32) 
retono: Retorno tipo float con valor en grados Fahrenheit
Salida esperada para valor en grados 12.5: 54.5
'''
def celsiusToFahrenheit(valor_grados):
    return valor_grados * 9 / 5 + 32

'''
2   Convertir grados Celsius a grados Kelvin

parametros de entrada: Parámetro tipo float con Valor en grados Celsius
aplicar formula: valor en celcius + 273.15	
retono: Retorno tipo float con valor en grados Kelvin
Salida esperada para valor en grados 12.5: 285.65
'''
def celsiusToKelvin(valor_grados):
    return valor_grados + 273.15

'''
3   Convertir grados Fahrenheit a grados Celsius

parametros de entrada: Parámetro tipo float con Valor en grados Fahrenheit
aplicar formula: ((valor en fahrenheit - 32) * (5 /9)
retono: Retorno tipo float con valor en grados Celsius 
Salida esperada para valor en grados 12.5: -10.83   
'''
def fahrenheitToCelcius(valor_grados):
    return  round(((valor_grados) - 32) * (5 /9),2)


'''
4   Convertir grados Fahrenheit a grados Kelvin	

Nombre: farenheitToKelvin
Parámetros de entrada: Parámetro tipo float con Valor en grados Fahrenheit
Formula: ((valor_grados - 32) * 5/9 + 273.15)
Retono: Retorno tipo float con valor en grados Kelvin
Salida esperada para valor en grados 12.5: 262.32
'''
def farenheitToKelvin(valor_grados):
    return round((valor_grados - 32) * 5/9 + 273.15,2)
    

'''
5   Convertir grados Kelvin a grados Celsius

Nombre: kelvinToCelsius
Parámetros de entrada: Parámetro tipo float con Valor en grados Kelvin
Formula: (valor_grados - 273.15)
Retono: Retorno tipo float con valor en grados Celsius
Salida esperada para valor en grados 12.5: -260.65
'''
def kelvinToCelsius(valor_grados):
    return (valor_grados - 273.15)

'''
6   Convertir grados Kelvin a grados Fahrenheit	
Nombre: kelvinToFarenheit
Parámetros de entrada: Parámetro tipo float con Valor en grados Kelvin
Formula: ((valor_grados -  273.15) * (9/5 + 32))
Retono: Retorno tipo float con valor en grados Fahrenheit
Salida esperada para valor en grados 12.5: -437.17
'''
def kelvinToFarenheit(valor_grados):
    return round((valor_grados -  273.15) * 9/5 + 32,2)


grados = float(input("Ingresa los grados de la temperatura :\t"))

#invocamos la función
print(f"El resultado de convertir {grados} celcius a Fahrenheit, es:\t {celsiusToFahrenheit(grados)}")
print(f"El resultado de convertir {grados} celcius a Kelvin, es:\t {celsiusToKelvin(grados)}")
print(f"El resultado de convertir {grados} Fahrenheit a Celsius, es:\t {fahrenheitToCelcius(grados)}")
print(f"El resultado de convertir {grados} Fahrenheit a Kelvin, es:\t {farenheitToKelvin(grados)}")
print(f"El resultado de convertir {grados} Kelvin a Celsius, es:\t {kelvinToCelsius(grados)}")
print(f"El resultado de convertir {grados} Kelvin a Fahrenheit, es:\t {kelvinToFarenheit(grados)}")
