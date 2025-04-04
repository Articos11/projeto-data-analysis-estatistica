import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

dados_idle = [
    9.1909, 9.8692, 9.2363, 9.8887, 10.0253, 9.0121, 9.6410, 11.2233, 8.6699, 9.5207,
    9.3437, 10.1790, 8.5018, 9.9240, 10.2698, 10.8572, 9.7404, 9.6893, 9.6376, 8.7033,
    9.2938, 10.2606, 9.4795, 8.9888, 8.4147, 6.5385, 9.1252, 7.7639, 9.7499, 12.6224,
    10.5259, 12.7709, 8.2550, 9.6464, 8.8338, 11.2852, 10.0112, 9.9306, 10.9588, 10.1797,
    9.8621, 9.1452, 9.6607, 8.2367, 8.5668, 8.7360, 10.6747, 10.6442, 9.4982, 8.2046,
    8.7733, 9.3662, 7.3480, 11.1260, 11.7480, 8.0641, 10.2881, 11.2382, 8.5552, 8.6407,
    10.9994, 9.4316, 8.6311, 10.8961, 12.0054, 12.2881, 10.4007, 10.2480, 10.6297, 10.5885,
    9.9235, 8.7854, 13.7949, 10.0499, 9.7302, 10.6651, 11.6158, 8.7185, 7.4474, 10.2098,
    11.4452, 8.9615, 8.8532, 9.6686, 9.5840, 9.7885, 11.6838, 9.1717, 11.2713, 8.4102,
    9.8014, 8.2892, 8.1164, 9.9213, 9.4725, 10.1777, 7.9336, 10.2716, 10.4550, 10.4669,
    10.6645, 8.7380, 10.2834, 10.5417, 9.5044, 10.7287, 11.1074, 9.7527, 9.7578, 8.3864,
    10.9066, 8.0825, 11.1309, 8.9391, 10.3617, 11.1634, 10.6548, 8.8425, 9.2338, 9.8071,
    8.4711, 6.8446, 9.8599, 10.7106, 9.3465, 9.4992, 10.8393, 12.5583, 9.7521, 9.4756,
    9.4133, 10.4600, 11.0919, 10.6427, 8.2310, 10.4486, 7.6875, 11.9924, 10.5424, 9.9526,
    10.8517, 9.7453, 10.4031, 10.3142, 11.1078, 9.4098, 8.2982, 10.6304, 10.5122, 11.4204,
    8.8507, 9.4479, 10.4363, 10.0775, 8.8455, 9.2746, 11.2161, 10.3456, 11.2071, 8.2725,
    10.2518, 10.9985, 8.8248, 8.3503, 8.9347, 10.1723, 9.1520, 11.5757, 8.9882, 10.0235,
    10.1516, 11.5230, 9.9293, 9.7187, 12.1184, 10.3105, 9.1047, 9.4516, 9.8104, 9.8246,
    10.3236, 10.5393, 8.7151, 8.9750, 12.1390, 9.4164, 11.5808, 11.7849, 8.3189, 11.3597,
    8.3214, 9.1792, 7.2526, 9.6062, 10.4731, 9.1423, 8.9796, 12.6885, 8.9049, 9.5932,
    9.4585, 7.5954, 10.4990, 9.5254, 11.3952, 10.8655, 9.8649, 11.1922, 9.1644, 9.7639,
    9.6113, 9.4023, 10.9853, 8.9627, 9.1211, 10.3541, 6.5416, 9.9387, 12.7051, 8.6285
]

media_esperada = 10 # H0: média == 10

# Dados da amostra
media_amostral = np.mean(dados_idle)
desvio_padrao = np.std(dados_idle, ddof=1)
n = len(dados_idle)

# Teste t
t_stat, p_valor = stats.ttest_1samp(dados_idle, popmean=media_esperada)

print(f'Média amostral: {media_amostral:.4f}')
print(f'Desvio padrão amostral: {desvio_padrao:.4f}')
print(f'Tamanho da amostra {n}')
print(f'Estatistica t: {t_stat:.4f}')
print(f'P-valor: {p_valor:.4f}')

alpha = 0.05 #nivel de significância com nível de confiância de 95%
if p_valor < alpha:
    print("Rejeita-se H0. Evidências indicam que a média é diferente de 10.")
else: 
    print("Não rejeitamos H0, não há evidência suficiente de que a média é diferente de 10.")


plt.hist(dados_idle, bins=20, edgecolor='black')
plt.axvline(media_esperada, color='red', linestyle='dashed', linewidth=1.5, label='Média esperada (10)')
plt.axvline(media_amostral, color='green', linestyle='dashed', linewidth=1.5, label=f'Média amostral ({media_amostral:.2f})')
plt.title('Distribuição dos valores Idle')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.legend()
plt.grid(True)
plt.show()