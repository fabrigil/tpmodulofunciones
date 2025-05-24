def calcular_IMC(peso, altura):
    valor_IMC = peso / (altura ** 2)
    redondeo_valor_IMC = round(valor_IMC, 2)

    if valor_IMC < 16:
        print(f"Delgadez severa, tiene un IMC de: {redondeo_valor_IMC}")
        return f"Delgadez severa, tiene un IMC de: {redondeo_valor_IMC}"
    elif 16 <= valor_IMC <= 16.99:
        print(f"Delgadez moderada, tiene un IMC de: {redondeo_valor_IMC}")
        return f"Delgadez moderada, tiene un IMC de: {redondeo_valor_IMC}"
    elif 17 <= valor_IMC <= 18.49:
        print(f"Delgadez aceptable, tiene un IMC de: {redondeo_valor_IMC}")
        return f"Delgadez aceptable, tiene un IMC de: {redondeo_valor_IMC}"
    elif 18.5 <= valor_IMC <= 24.99:
        print(f"Peso normal, tiene un IMC de: {redondeo_valor_IMC}")
        return f"Peso normal, tiene un IMC de: {redondeo_valor_IMC}"
    elif 25 <= valor_IMC <= 29.99:
        print(f"Sobrepeso, tiene un IMC de: {redondeo_valor_IMC}")
        return f"Sobrepeso, tiene un IMC de: {redondeo_valor_IMC}"
    elif 30 <= valor_IMC <= 34.99:
        print(f"Obesidad tipo I, tiene un IMC de: {redondeo_valor_IMC}")
        return f"Obesidad tipo I, tiene un IMC de: {redondeo_valor_IMC}"
    elif 35 <= valor_IMC <= 39.99:
        print(f"Obesidad tipo II, tiene un IMC de: {redondeo_valor_IMC}")
        return f"Obesidad tipo II, tiene un IMC de: {redondeo_valor_IMC}"
    elif 40 <= valor_IMC <= 49.99:
        print(f"Obesidad tipo III o mórbida, tiene un IMC de: {redondeo_valor_IMC}")
        return f"Obesidad tipo III o mórbida, tiene un IMC de: {redondeo_valor_IMC}"
    elif valor_IMC >= 50:
        print(f"Obesidad tipo IV o extrema, tiene un IMC de: {redondeo_valor_IMC}")
        return f"Obesidad tipo IV o extrema, tiene un IMC de: {redondeo_valor_IMC}"

def calcular_porcentaje_grasa(peso, altura, edad, genero):
    valor_IMC = peso / (altura ** 2)

    while genero == 1:
        valor_genero = 10.8
        grasa_corporal = 1.2 * valor_IMC + 0.23 * edad - 5.4 - valor_genero
        redondeo_grasa_corporal = round(grasa_corporal, 2)

        if grasa_corporal < 11:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado un deportista de alto rendimiento ya que tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado un deportista de alto rendimiento ya que tiene un porcentaje de: {redondeo_grasa_corporal}%"
        if grasa_corporal > 24:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado una persona con obesidad ya que tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado una persona con obesidad ya que tiene un porcentaje de: {redondeo_grasa_corporal}%"

        if 20 <= edad <= 29 and 11 <= grasa_corporal <= 20:
            print(f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
        elif 20 <= edad <= 29 and grasa_corporal > 20:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"

        if 30 <= edad <= 39 and 12 <= grasa_corporal <= 21:
            print(f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
        elif 30 <= edad <= 39 and 12 > grasa_corporal > 21:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"

        if 40 <= edad <= 49 and 14 <= grasa_corporal <= 23:
            print(f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
        elif 40 <= edad <= 49 and 14 > grasa_corporal > 23:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"

        if 50 <= edad <= 59 and 15 <= grasa_corporal <= 24:
            print(f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
        elif 50 <= edad <= 59 and grasa_corporal < 15:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
        break

    while genero == 0:
        valor_genero = 0
        grasa_corporal = 1.2 * valor_IMC + 0.23 * edad - 5.4 - valor_genero
        redondeo_grasa_corporal = round(grasa_corporal, 2)

        if grasa_corporal < 16:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado una deportista de alto rendimiento ya que tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado una deportista de alto rendimiento ya que tiene un porcentaje de: {redondeo_grasa_corporal}%"
        if grasa_corporal > 31:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado una persona con obesidad ya que tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado una persona con obesidad ya que tiene un porcentaje de: {redondeo_grasa_corporal}%"

        if 20 <= edad <= 29 and 16 <= grasa_corporal <= 28:
            print(f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
        elif 20 <= edad <= 29 and grasa_corporal > 28:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"

        if 30 <= edad <= 39 and 17 <= grasa_corporal <= 29:
            print(f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
        elif 30 <= edad <= 39 and 17 > grasa_corporal > 29:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"

        if 40 <= edad <= 49 and 18 <= grasa_corporal <= 30:
            print(f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
        elif 40 <= edad <= 49 and 18 > grasa_corporal > 30:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"

        if 50 <= edad <= 59 and 19 <= grasa_corporal <= 31:
            print(f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
        elif 50 <= edad <= 59 and grasa_corporal < 19:
            print(f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%")
            return f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
        break

def calcular_calorias_en_reposo(peso, altura, edad, genero):

    while genero == 1:
        valor_genero = 5
        valor_tmb = 10 * peso + 6.25 * altura - 5 * edad + valor_genero
        redondeo_valor_tmb = round(valor_tmb, 2)
        print(f"Su tasa metabólica basal es de: {redondeo_valor_tmb} calorías")
        return f"Su tasa metabólica basal es de: {redondeo_valor_tmb} calorías"

    while genero == 0:
        valor_genero = -161
        valor_tmb = 10 * peso + 6.25 * altura - 5 * edad + valor_genero
        redondeo_valor_tmb = round(valor_tmb, 2)
        print(f"Su tasa metabólica basal es de: {redondeo_valor_tmb} calorías")
        return f"Su tasa metabólica basal es de: {redondeo_valor_tmb} calorías"

def calcular_calorias_en_actividad(peso, altura, edad, genero, valor_actividad):

    while genero == 1:
        valor_genero = 5
        valor_tmb = 10 * peso + 6.25 * altura - 5 * edad + valor_genero

        if valor_actividad == 1:
            valor_tmb_actividad = valor_tmb * 1.2
            redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
            print(f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías")
            return f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
        elif valor_actividad == 2:
            valor_tmb_actividad = valor_tmb * 1.375
            redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
            print(f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías")
            return f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
        elif valor_actividad == 3:
            valor_tmb_actividad = valor_tmb * 1.55
            redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
            print(f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías")
            return f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
        elif valor_actividad == 4:
            valor_tmb_actividad = valor_tmb * 1.725
            redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
            print(f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías")
            return f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
        elif valor_actividad == 5:
            valor_tmb_actividad = valor_tmb * 1.9
            redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
            print(f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías")
            return f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
        break

    while genero == 0:
        valor_genero = -161
        valor_tmb = 10 * peso + 6.25 * altura - 5 * edad + valor_genero

        if valor_actividad == 1:
            valor_tmb_actividad = valor_tmb * 1.2
            redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
            print(f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías")
            return f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
        elif valor_actividad == 2:
            valor_tmb_actividad = valor_tmb * 1.375
            redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
            print(f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías")
            return f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
        elif valor_actividad == 3:
            valor_tmb_actividad = valor_tmb * 1.55
            redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
            print(f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías")
            return f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
        elif valor_actividad == 4:
            valor_tmb_actividad = valor_tmb * 1.725
            redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
            print(f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías")
            return f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
        elif valor_actividad == 5:
            valor_tmb_actividad = valor_tmb * 1.9
            redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
            print(f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías")
            return f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
        break

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, genero):

    while genero == 1:
        valor_genero = 5
        valor_tmb = 10 * peso + 6.25 * altura - 5 * edad + valor_genero
        calorias_minimas_recomendadas = 80 * valor_tmb / 100
        calorias_maximas_recomendadas = 85 * valor_tmb / 100
        redondeo_calorias_minimas_recomendadas = round(calorias_minimas_recomendadas, 2)
        redondeo_calorias_maximas_recomendadas = round(calorias_maximas_recomendadas, 2)
        print(f"Para adelgazar es recomendado que consumas entre: {redondeo_calorias_minimas_recomendadas} y {redondeo_calorias_maximas_recomendadas} calorías al día")
        return f"Para adelgazar es recomendado que consumas entre: {redondeo_calorias_minimas_recomendadas} y {redondeo_calorias_maximas_recomendadas} calorías al día"

    while genero == 0:
        valor_genero = -161
        valor_tmb = 10 * peso + 6.25 * altura - 5 * edad + valor_genero
        calorias_minimas_recomendadas = 80 * valor_tmb / 100
        calorias_maximas_recomendadas = 85 * valor_tmb / 100
        redondeo_calorias_minimas_recomendadas = round(calorias_minimas_recomendadas, 2)
        redondeo_calorias_maximas_recomendadas = round(calorias_maximas_recomendadas, 2)
        print(f"Para adelgazar es recomendado que consumas entre: {redondeo_calorias_minimas_recomendadas} y {redondeo_calorias_maximas_recomendadas} calorías al día")
        return f"Para adelgazar es recomendado que consumas entre: {redondeo_calorias_minimas_recomendadas} y {redondeo_calorias_maximas_recomendadas} calorías al día"