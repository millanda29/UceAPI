# InferenceService.py
import os
from openai import OpenAI
from ec.llm.utils.const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT


class InferenceService:
    def __init__(self):
        self.__model = os.getenv('OPENAI_MODEL', 'text-davinci-003')
        self.__openai_client = OpenAI()
        self.__prompt_template_goty = 'Quien gano el mundial de fútbol en {year}?'
        self.__prompt_template_binary_to_decimal = 'Convert {binary_number} to decimal.'
        self.__prompt_template_binary_to_octal = 'Convierte el numero {decimal_number} a octal'
        self.__prompt_template_who_is = 'Quien es {persona}?'

    def __inference(self, prompt):
        return CLEAN_TEXT(self.__openai_client.completions.create(
            model=self.__model,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        ).choices[0].text)

    def invoke_goty(self, year: str) -> str:
        prompt = self.__prompt_template_goty.format(year=year)
        return self.__inference(prompt)

    def invoke_binary_to_decimal(self, binary_number: str) -> str:
        prompt = self.__prompt_template_binary_to_decimal.format(binary_number=binary_number)
        return self.__inference(prompt)

    def invoke_binary_to_octal(self, decimal_number: str) -> str:
        prompt = self.__prompt_template_binary_to_octal.format(decimal_number=decimal_number)
        return self.__inference(prompt)

    def invoke_who_is(self, persona: str) -> str:
        prompt = self.__prompt_template_who_is.format(persona=persona)
        return self.__inference(prompt)
