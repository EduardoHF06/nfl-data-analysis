# nfl-data-analysis
# Análise Exploratória: Fatores de Vitória na NFL

## Sobre o Projeto
Este é um projeto prático de Análise Exploratória de Dados (EDA) focado em descobrir quais métricas estatísticas têm maior impacto no número de vitórias das franquias da NFL. 

O objetivo principal foi pegar dados brutos de desempenho (jardas passadas, corridas, turnovers e performance defensiva) e transformá-los em informações visuais claras para responder a uma pergunta de negócio: **o que realmente faz um time vencer?**

## Tecnologias e Bibliotecas
* **Python 3** (Linguagem principal)
* **Pandas & NumPy** (Manipulação, limpeza e estruturação de dados)
* **Matplotlib & Seaborn** (Criação de gráficos e visualização de dados)

## O que foi desenvolvido
Para simular um cenário real de análise de dados, apliquei os seguintes passos neste projeto:
1. **Coleta e Estruturação:** Importação dos dados estatísticos das equipes.
2. **Limpeza de Dados (Data Cleaning):** Tratamento de valores ausentes (Nulo/NaN) utilizando a mediana da liga para não distorcer a análise de desempenho de jardas e turnovers.
3. **Análise de Correlação:** Cruzamento matemático entre as métricas de jogo e a coluna alvo ("Vitórias") para identificar os fatores de maior peso.
4. **Visualização:** Geração de mapas de calor (Heatmaps) e gráficos de dispersão para facilitar a leitura dos resultados por pessoas não-técnicas.

## Principais Insights
Através dos gráficos gerados pelo script, foi possível identificar que:
* **Defesa ganha campeonato:** Existe uma forte correlação positiva entre a pressão no quarterback adversário (Sacks) e o número de vitórias na temporada regular.
* **O peso do erro:** Turnovers sofridos apresentam correlação negativa com as vitórias, reforçando que a proteção da posse de bola é matematicamente mais relevante que o volume total de jardas passadas em alguns cenários.

## Como executar este projeto
1. Clone este repositório: `git clone https://github.com/EduardoHF06/nfl-data-analysis.git`
2. Instale as dependências: `pip install pandas numpy matplotlib seaborn`
3. Execute o script principal: `python nfl_analysis.py`
