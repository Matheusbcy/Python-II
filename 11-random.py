import random

# 1 - Seleciona valor aleatorio de uma lista
list1 = [
    "Toin",
    "Xandao",
    "Didico",
    "Hadopp",
    "Hamud",
    "Kelvinho",
    "GilbertPet",
    "Luiz Vito",
    "Pedro",
    "JOTTA",
]
print(random.choice(list1))

# 2 - Gera um numero aleatorio em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)

# 3 - Seleciona caractere aleatorio de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatorio
# Sintaxe: random.sample(sequencia, tamanho)
time1 = random.sample(list1, 5)
time2 = [jogador for jogador in list1 if jogador not in time1]

print(f"Time 1: {time1}")
print(f"Time 2: {time2}")