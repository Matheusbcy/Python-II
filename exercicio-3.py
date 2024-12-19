"""
Verificando conteudo da String
-> Escreva um programa em Python para verificar se uma string
contém apenas um determinado conjunto de caracteres (neste caso, a-z,
A-Z e 0-9).
"""

import re

text = "Python123"

pattern = r'^[a-zA-Z0-9]*$'

if re.match(pattern, text):
    print("A string contem apenas caracteres permitidos.")
else:
    print("A string contem caracteres nao permitidos.")