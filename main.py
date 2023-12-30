# main.py
from dotenv import load_dotenv
import os
from ec.llm.service.InferenceService import InferenceService

if __name__ == '__main__':
    load_dotenv('secrets/.env')
    # print(os.getenv('OPENAI_API_KEY'))

    # Ejemplo: Obtener GOTY para el año 2017
    #goty_result = InferenceService().invoke_goty('2018')
    #print(f"GOTY Result: {goty_result}")

    # Ejemplo: Convertir número binario a decimal
    #binary_to_decimal_result = InferenceService().invoke_binary_to_decimal('1101')
    #print(f"Binary to Decimal Result: {binary_to_decimal_result}")

    # Ejemplo: Convertir número binario a float
    #binary_to_float_result = InferenceService().invoke_binary_to_float('101010')
    #print(f"Binary to Float Result: {binary_to_float_result}")

    # Ejemplo: Quien es persona
    print(f"Ingrese el nombre famoso: ")
    nombre = input()
    who_is_result = InferenceService().invoke_who_is(nombre)
    print(f"Who is: {who_is_result}")