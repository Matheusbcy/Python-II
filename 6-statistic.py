import statistics

# 1 - Aplicar a média
print(statistics.mean([2, 4, 5, 6, 10]))

# 2 - Aplicar a mediana
print(statistics.median([2, 4, 5, 6, 10]))
print(statistics.median([2, 2, 4, 7, 8, 10]))

# 3 - Aplicar a moda
print(statistics.mode([2, 4, 5, 6, 2, 2, 10 ,9, 2, 2, 10 ,9]))

# 4 - Desvio padrão
"""
- Quanto mais proximo de 0 for o desvio padrão,
significa que os dados do conunto estão menos dispersos
"""
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))
#F066