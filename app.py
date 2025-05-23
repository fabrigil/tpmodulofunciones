import subprocess
import sys

while True:
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Bienvenido a la calculadora de índices corporales! Elija una opción para calcular:")
    print("1. Calcular índice de masa corporal (IMC)")
    print("2. Calcular porcentaje de grasa corporal")
    print("3. Calcular tasa metabólica basal (TMB)")
    print("4. Calcular tasa metabólica basal (TMB) según actividad física")
    print("5. Calcular calorías diarias para adelgazar")
    print("6. Salir de la aplicación")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    opcion = input("Opción: ")
    if opcion == "1":
        subprocess.run([sys.executable, 'consola_calculo_imc.py'])
    elif opcion == "2":
        subprocess.run([sys.executable, 'consola_calculo_porcentaje_grasa.py'])
    elif opcion == "3":
        subprocess.run([sys.executable, 'consola_calculo_calorias_reposo.py'])
    elif opcion == "4":
        subprocess.run([sys.executable, 'consola_calculo_calorias_actividad.py'])
    elif opcion == "5":
        subprocess.run([sys.executable, 'consola_calculo_calorias_adelgazar.py'])
    elif opcion == "6":
        print("Saliendo de la aplicación...")
        break
    else:
        print("Opción ingresada no válida, por favor elija una opción válida para calcular")