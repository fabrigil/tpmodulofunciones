def calcular_IMC(peso, altura):
    valor_IMC = peso / (altura ** 2)
    redondeo_valor_IMC = round(valor_IMC, 2)

    if valor_IMC < 16:
        mensaje = f"Delgadez severa, tiene un IMC de: {redondeo_valor_IMC}"
    elif valor_IMC < 17:
        mensaje = f"Delgadez moderada, tiene un IMC de: {redondeo_valor_IMC}"
    elif valor_IMC < 18.5:
        mensaje = f"Delgadez aceptable, tiene un IMC de: {redondeo_valor_IMC}"
    elif valor_IMC < 25:
        mensaje = f"Peso normal, tiene un IMC de: {redondeo_valor_IMC}"
    elif valor_IMC < 30:
        mensaje = f"Sobrepeso, tiene un IMC de: {redondeo_valor_IMC}"
    elif valor_IMC < 35:
        mensaje = f"Obesidad tipo I, tiene un IMC de: {redondeo_valor_IMC}"
    elif valor_IMC < 40:
        mensaje = f"Obesidad tipo II, tiene un IMC de: {redondeo_valor_IMC}"
    elif valor_IMC < 50:
        mensaje = f"Obesidad tipo III o mórbida, tiene un IMC de: {redondeo_valor_IMC}"
    else:
        mensaje = f"Obesidad tipo IV o extrema, tiene un IMC de: {redondeo_valor_IMC}"

    print(mensaje)
    return mensaje

def calcular_porcentaje_grasa(peso, altura, edad, genero):
    valor_IMC = peso / (altura ** 2)
    grasa_corporal = 1.2 * valor_IMC + 0.23 * edad - 5.4 - (10.8 if genero == 1 else 0)
    redondeo_grasa_corporal = round(grasa_corporal, 2)

    if genero == 1:
        if grasa_corporal < 11:
            mensaje = f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado un deportista de alto rendimiento ya que tiene un porcentaje de: {redondeo_grasa_corporal}%"
        elif grasa_corporal > 24:
            mensaje = f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado una persona con obesidad ya que tiene un porcentaje de: {redondeo_grasa_corporal}%"
        else:
            if 20 <= edad <= 29:
                rango = (11, 20)
            elif 30 <= edad <= 39:
                rango = (12, 21)
            elif 40 <= edad <= 49:
                rango = (14, 23)
            elif 50 <= edad <= 59:
                rango = (15, 24)
    else:
        if grasa_corporal < 16:
            mensaje = f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado una deportista de alto rendimiento ya que tiene un porcentaje de: {redondeo_grasa_corporal}%"
        elif grasa_corporal > 31:
            mensaje = f"Fuera del rango de porcentaje de grasa corporal recomendado, puede ser considerado una persona con obesidad ya que tiene un porcentaje de: {redondeo_grasa_corporal}%"
        else:
            if 20 <= edad <= 29:
                rango = (16, 28)
            elif 30 <= edad <= 39:
                rango = (17, 29)
            elif 40 <= edad <= 49:
                rango = (18, 30)
            elif 50 <= edad <= 59:
                rango = (19, 31)
    if grasa_corporal < rango[0] or grasa_corporal > rango[1]:
        mensaje = f"Fuera del rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"
    else:
        mensaje = f"Rango de porcentaje de grasa corporal recomendado para su edad, tiene un porcentaje de: {redondeo_grasa_corporal}%"

    print(mensaje)
    return mensaje

def calcular_calorias_en_reposo(peso, altura, edad, genero):
    valor_tmb = 10 * peso + 6.25 * altura - 5 * edad + (5 if genero == 1 else -161)
    redondeo_valor_tmb = round(valor_tmb, 2)
    mensaje = f"Su tasa metabólica basal es de: {redondeo_valor_tmb} calorías"
    print(mensaje)
    return mensaje

def calcular_calorias_en_actividad(peso, altura, edad, genero, valor_actividad):
    tipos = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }

    tipo = tipos[valor_actividad]
    valor_tmb = 10 * peso + 6.25 * altura - 5 * edad + (5 if genero == 1 else -161)
    valor_tmb_actividad = valor_tmb * tipo
    redondeo_valor_tmb_actividad = round(valor_tmb_actividad, 2)
    mensaje = f"Su tasa metabólica basal según su actividad física es de: {redondeo_valor_tmb_actividad} calorías"
    print(mensaje)
    return mensaje

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, genero):
    valor_tmb = 10 * peso + 6.25 * altura - 5 * edad + (5 if genero == 1 else -161)
    calorias_minimas_recomendadas = 80 * valor_tmb / 100
    calorias_maximas_recomendadas = 85 * valor_tmb / 100
    redondeo_calorias_minimas_recomendadas = round(calorias_minimas_recomendadas, 2)
    redondeo_calorias_maximas_recomendadas = round(calorias_maximas_recomendadas, 2)
    mensaje = f"Para adelgazar es recomendado que consumas entre: {redondeo_calorias_minimas_recomendadas} y {redondeo_calorias_maximas_recomendadas} calorías al día"
    print(mensaje)
    return mensaje