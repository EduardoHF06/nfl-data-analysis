#AnaliseNFL

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



#Simular os dados de 10 times da NFL
data = {
    'Time': ['Chiefs', 'Eagles', '49ers', 'Bengals', 'Bills', 'Cowboys', 'Ravens', 'Dolphins', 'Lions', 'Jaguars'],
    'Vitorias': [14, 14, 13, 12, 13, 12, 10, 9, 9, 9],
    'Jardas_Passe_Por_Jogo': [297.8, 241.5, 226.8, np.nan, 258.1, 219.8, 178.8, 265.4, 251.8, 232.9],
    'Jardas_Corrida_Por_Jogo': [115.9, 147.6, 138.8, 95.5, 139.5, 131.7, 160.0, 99.2, 128.0, 124.5],
    'Turnovers_Sofridos': [23, 19, 17, 18, 27, np.nan, 21, 21, 15, 22],
    'Sacks_Defesa': [55, 70, 44, 30, 40, 54, 48, 40, 39, 35]
}

df = pd.DataFrame(data)
print("--- Dados Brutos ---")
print(df.head())


print("\n--- Limpeza de Dados ---")
print(f"Valores nulos antes do tratamento:\n{df.isnull().sum()}")

df['Jardas_Passe_Por_Jogo'] = df['Jardas_Passe_Por_Jogo'].fillna(df['Jardas_Passe_Por_Jogo'].median())
df['Turnovers_Sofridos'] = df['Turnovers_Sofridos'].fillna(df['Turnovers_Sofridos'].median())

print(f"\nValores nulos após o tratamento:\n{df.isnull().sum()}")

estatisticas = ['Vitorias', 'Jardas_Passe_Por_Jogo', 'Jardas_Corrida_Por_Jogo', 'Turnovers_Sofridos', 'Sacks_Defesa']
correlacao = df[estatisticas].corr()
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.heatmap(correlacao, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title
