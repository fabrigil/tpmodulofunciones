import calculadora_indices as calc
from calculadora_indices import calcular_porcentaje_grasa

if __name__ == "__main__":
    try:
        peso = float(input("Ingrese su peso en kg: "))
        if peso <= 0:
            peso = float(input("Peso ingresado no válido, por favor ingrese su peso válido en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
        if altura <= 0:
            altura = float(input("Altura ingresada no válida, por favor ingrese su altura válida en metros: "))
        if altura.is_integer():
            altura = float(input("Altura ingresada en centímetros, por favor ingrese su altura en metros: "))
        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
            edad = int(input("Edad ingresada no válida, por favor ingrese su edad válida: "))
        genero = int(input("Ingrese su género: 1 si es masculino, 0 si es femenino: "))
        if genero != 1 and genero != 0:
            genero = int(input("Género no válido, ingrese su género: 1 si es masculino, 0 si es femenino: "))
        grasa_corporal = calcular_porcentaje_grasa(peso, altura, edad, genero)
        resultado = grasa_corporal
        with open("resultado_temp.txt", "w", encoding='utf-8-sig') as archivo:
            archivo.write(str(resultado))
    except ValueError:
        print("Error: Ingrese un número válido para peso y/o altura y/o edad")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        input("Presione cualquier tecla para volver al menú...")