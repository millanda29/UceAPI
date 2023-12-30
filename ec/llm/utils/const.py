# const.py
import re

TEMPERATURE = 0.2
MAX_TOKENS = 50

def CLEAN_TEXT(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()
