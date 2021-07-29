
# ejercicio número 1
"""
crear una variable donde deberás asignar tu fecha de nacimiento como entero
declarar otra variable con tu nombre
en una tercera variable concatenar las dos variables anteriores e imprimir el resultado en consola utilizando interpolación.
el mensaje debe tener el siguiente formato: mi nombre es <aqui tu nombre> y mi fecha de nacimiento es el año <aquí tu fecha de nacimiento>
"""
print("Ejercicio #1")
anio= 1980
nombre= "Minerva"
print(f"Mi nombre es: {nombre} y mi año de nacimiento es: {anio}")
print("")


# ejercicio número 2
"""
definir en una variable de tipo entero tu mes de nacimiento
tomando el mes actual como referencia imprimir en pantalla si ya cumpliste años en este año(2021)
el mensaje debe tener el siguiente formato: Este anio ya cumpli anios? True|False
"""
print("Ejercicio #2")
mes_nacimiento= 11
mes_actual=7
print(f"En este año ya cumpli años ya que soy del mes de noviembre? {mes_nacimiento < mes_actual}")
print("")

# ejercicio número 3
"""
definir una variable tipo booleana donde se indique si te gustan los gatos
definir una variable donde indique si te gustan los perros
definir una tercera variable donde se almacene el valor booleano de si te gustan los gatos y también los perros.
imprimir en consola un mensaje con el siguiente formato:
Es verdad que me gustan los gatos y los perros? <aqui el valor de tu tercer variable>
"""
print("Ejercicio #3")
megustanG = False
megustanP = False
union = megustanG and megustanP
print(f"En verdad me gustan los gatos y los perros?: {union}")
print("")

# ejercicio número 4
"""
usando el método input, método print y el operador de pertenencia "in"
hacer el codigo para que se pida ingresar el nombre y tu mes de 
cumpleaños(recuerda que este valor se recibe como string, tendras que hacer casting a int)
definir una lista llamada "primeros_seis_meses_anio"  con los siguientes elementos: 1, 2, 3 , 4, 5, 6
imprimir en consola un mensaje con el siguiente formato:
Hola mi nombre es <aqui tu nombre>. Cumplo años en los primeros seis meses del año? <valor booleano aqui>
"""
print("Ejercicio #4")
nombre = input("Ingresa tu nombre: ")
mes = input("Ingresa tu mes de nacimiento: ")
mes_int=int(mes)
primeros_seis_meses_anio=[1,2,3,4,5,6]
seEncuentraValor= 11 in primeros_seis_meses_anio
print(f"Hola mi nombre es: {nombre}. Cumplo años en los primeros meses del año? : {seEncuentraValor}" )
print("")

# ejercicio 5
"""
hacer lo mismo que el ejercicio 4 pero usar un diccionario llamado "mi_info" para almacenar
las entradas(nombre, mes de nacimiento).
"""
print("Ejercicio #5")
"""nombre = input("Ingresa tu nombre: ")
mes = input("Ingresa tu mes de nacimiento")
mes_int=int(mes)"""

mi_info={"nom":"Minerva", "nov": 11}
primeros_seis_meses_anio=[1,2,3,4,5,6]
seEncuentraValor= 11 in primeros_seis_meses_anio
print(f"Hola mi nombre es: {mi_info}. Cumplo años en los primeros meses del año? : {seEncuentraValor}" )