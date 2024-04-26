import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler os dados da planilha do Excel
df = pd.read_excel(r'C:\Users\Claudio M. Antonio\Downloads\Lista_Bilionarios_Forbes_2023.xlsx')

# Converter a coluna "Patrimonio" para tipo numérico
df['Patrimonio'] = df['Patrimonio'].str.replace('$', '').str.replace('B', '').astype(float)

# Agrupar os dados por setor e somar o valor do patrimônio
agrupado = df.groupby('Setor')['Patrimonio'].sum().reset_index()

# Ordenar o DataFrame em ordem decrescente pelo valor do patrimônio
agrupado = agrupado.sort_values('Patrimonio', ascending=False)

# Configurar o estilo do gráfico
sns.set(style='whitegrid')

# Criar o gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(data=agrupado, x='Setor', y='Patrimonio', palette='Blues_d')

# Configurar os rótulos dos eixos
plt.xlabel('Setor')
plt.ylabel('Faturamento Total (em bilhões de dólares)')

# Configurar o título do gráfico
plt.title('Faturamento Total agrupado por Setor (100 Bilionários da Forbes 2023)')

# Rotacionar os rótulos do eixo x para facilitar a leitura
plt.xticks(rotation=45, ha='right')

# Exibir o gráfico
plt.show()
