# main.py
from dotenv import load_dotenv
import os
from ec.llm.service.InferenceService import InferenceService

if __name__ == '__main__':
    load_dotenv('secrets/.env')
    print(os.getenv('OPENAI_API_KEY'))

    # Ejemplo: Obtener GOTY para el año 2017
    goty_result = InferenceService().invoke_goty('2017')
    print(f"GOTY Result: {goty_result}")

    # Ejemplo: Convertir número binario a decimal
    binary_to_decimal_result = InferenceService().invoke_binary_to_decimal('1101')
    print(f"Binary to Decimal Result: {binary_to_decimal_result}")
