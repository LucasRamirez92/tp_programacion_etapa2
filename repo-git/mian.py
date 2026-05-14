"""
Tp etapa 1 
div 114
turno mañana
grupo 11
Lucas Ramirez
Alejandro Aburto
Abel Cruz limachi

Parte 1:

Utilizando el paradigma estructurado, generar un archivo denominado “principal.py” en el
que se desarrollará la ejecución del bucle principal de nuestro programa. El mismo debe
permitir el acceso al usuario mediante el ingreso de un nombre y una contraseña o en caso
de que el mismo no se encuentre en la base de dato, su registro.

Una vez haya ingresado exitosamente el usuario, se deberá mostrar por consola un menú de
opciones que incluya la posibilidad de:

a) Proyectos: Generación y gestión de proyectos.
b) Tablas: creación y modificación de tablas.
c) Variables: Creación, carga y modificación de variables.
d) Mostrar: Mostrar por pantalla información disponible en una tabla.
e) Estadística: Conteos o frecuencias. Máximos y mínimos. Medidas de tendencia
central: promedios aritméticos y geométricos. Medidas de dispersión. Medidas de
posición.
f) Salir: Finalizar la ejecución del programa

Todo ingreso de información por parte del usuario debe contar con las validaciones
correspondientes.

No se permite la utilización de funciones creadas por terceros con excepción de casteo, len y
range. Toda función utilizada debe ser implementada en un módulo que sea parte del
programa

"""


import validaciones 

usuario = "admin"
contraseña = "1234"

usuario_ingresado = input("Ingrese su nombre de usuario: ")
contraseña_ingresada = input("Ingrese su contraseña: ")

if usuario_ingresado != usuario and contraseña_ingresada != contraseña:
    print("Usuario no registrado. Procediendo al registro.")
    nuevo_usuario = input("Ingrese un nuevo nombre de usuario: ")
    nueva_contraseña = input("Ingrese una nueva contraseña: ")
    print(f"Usuario '{nuevo_usuario}' registrado exitosamente. Ahora puede iniciar sesión.")

while usuario_ingresado != usuario or contraseña_ingresada != contraseña:
    print("Usuario o contraseña incorrectos. Intente nuevamente.")
    usuario_ingresado = input("Ingrese su nombre de usuario: ")
    contraseña_ingresada = input("Ingrese su contraseña: ")

print(f"¡Bienvenido, {usuario_ingresado}!")

# menu desplegable

while True:
    print("\nMenú de opciones:")
    print("a) Proyectos: Generación y gestión de proyectos.")
    print("b) Tablas: creación y modificación de tablas.")
    print("c) Variables: Creación, carga y modificación de variables.")
    print("d) Mostrar: Mostrar por pantalla información disponible en una tabla.")
    print("e) Estadística: Conteos o frecuencias. Máximos y mínimos. Medidas de tendencia central: promedios aritméticos y geométricos. Medidas de dispersión. Medidas de posición.")
    print("f) Salir: Finalizar la ejecución del programa.")

    opcion = input("Seleccione una opción (a-f): ")

    if opcion == "a":
        print("→ Proyectos")
    elif opcion == "b":
        print("→ Tablas")
    elif opcion == "c":
        print("→ Variables")
    elif opcion == "d":
        print("→ Mostrar")
    elif opcion == "e":
        print("→ Estadística")
    elif opcion == "f":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Ingrese una letra entre a y f.")


"""

"""
