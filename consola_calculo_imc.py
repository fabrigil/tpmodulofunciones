import calculadora_indices as calc
from calculadora_indices import calcular_IMC

if __name__ == "__main__":
    try:
        peso = float(input("Ingrese su peso en kg: "))
        while peso <= 0:
            peso = float(input("Peso ingresado no válido, por favor ingrese su peso válido en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
        while altura <= 0:
            altura = float(input("Altura ingresada no válida, por favor ingrese su altura válida en metros: "))
        while altura.is_integer():
            altura = float(input("Altura ingresada en centímetros, por favor ingrese su altura en metros: "))
        valor_IMC = calcular_IMC(peso, altura)
    except ValueError:
        print("Error: Ingrese un número válido para peso y/o altura")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        input("Presione cualquier tecla para volver al menú...")