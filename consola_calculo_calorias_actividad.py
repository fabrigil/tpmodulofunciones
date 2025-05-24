import calculadora_indices as calc
from calculadora_indices import calcular_calorias_en_actividad

if __name__ == "__main__":
    try:
        peso = float(input("Ingrese su peso en kg: "))
        while peso <= 0:
            peso = float(input("Peso ingresado no válido, por favor ingrese su peso válido en kg: "))
        altura = int(input("Ingrese su altura en centímetros: "))
        while altura <= 0:
            altura = int(input("Altura ingresada no válida, por favor ingrese su altura válida en centímetros: "))
        edad = int(input("Ingrese su edad: "))
        while edad <= 0:
            edad = int(input("Edad ingresada no válida, por favor ingrese su edad válida: "))
        genero = int(input("Ingrese su género: 1 si es masculino, 0 si es femenino: "))
        while genero != 1 and genero != 0:
            genero = int(input("Género no válido, ingrese su género: 1 si es masculino, 0 si es femenino: "))
        valor_actividad = int(input("Ingrese según su nivel de actividad física a la semana: 1 poco o ningún ejercicio, 2 ejercicio ligero (1 a 3 días a la semana), 3 ejercicio moderado (3 a 5 días a la semana), 4 deportista (6 a 7 días a la semana) y 5 atleta (entrenamientos mañana y tarde): "))
        while valor_actividad != 1 and valor_actividad != 2 and valor_actividad != 3 and valor_actividad != 4 and valor_actividad != 5:
            valor_actividad = int(input("Nivel de actividad física a la semana no válido, ingrese según su nivel de actividad física a la semana: 1 poco o ningún ejercicio, 2 ejercicio ligero (1 a 3 días a la semana), 3 ejercicio moderado (3 a 5 días a la semana), 4 deportista (6 a 7 días a la semana) y 5 atleta (entrenamientos mañana y tarde): "))
        valor_tmb_actividad = calcular_calorias_en_actividad(peso, altura, edad, genero, valor_actividad)
        resultado = valor_tmb_actividad
        with open("resultado_temp.txt", "w", encoding='utf-8-sig') as archivo:
            archivo.write(str(resultado))
    except ValueError:
        print("Error: Ingrese un número válido para peso y/o altura y/o edad")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        input("Presione cualquier tecla para volver al menú...")