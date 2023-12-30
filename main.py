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
    binary_number = '1101'
    inference_service = InferenceService()
    binary_to_decimal_result = inference_service.invoke_binary_to_decimal(binary_number)
    print(f"Binary to Decimal Result: {binary_to_decimal_result}")

    # Ejemplo: Convertir número binario a octal
    binary_to_octal_result = inference_service.invoke_binary_to_octal(binary_to_decimal_result)
    print(f"Binary to Octal Result: {binary_to_octal_result}")

    # Ejemplo: Quien es persona
    #print(f"Ingrese el nombre famoso: ")
    #nombre = input()
    #who_is_result = InferenceService().invoke_who_is(nombre)
    #print(f"Who is: {who_is_result}")