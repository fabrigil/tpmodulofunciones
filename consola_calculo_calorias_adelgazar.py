import calculadora_indices as calc
from calculadora_indices import consumo_calorias_recomendado_para_adelgazar

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
        calorias_recomendadas = consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, genero)
        resultado = calorias_recomendadas
        with open("resultado_temp.txt", "w", encoding='utf-8-sig') as archivo:
            archivo.write(str(resultado))
    except ValueError:
        print("Error: Ingrese un número válido para peso y/o altura y/o edad")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        input("Presione cualquier tecla para volver al menú...")