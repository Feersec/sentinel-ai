# 🤖 SentinelAI - Detector de URLs Maliciosas

SentinelAI é uma ferramenta de linha de comando construída em Python que utiliza um modelo de Machine Learning (Random Forest) para detectar se uma URL é benigna ou maliciosa (phishing/malware).

Este projeto foi desenvolvido como uma introdução prática à aplicação de Inteligência Artificial no campo da Cibersegurança.

## ✨ Funcionalidades

-   Análise de URLs em tempo real.
-   Classificação de URLs como 'BENIGN' ou 'BAD'.
-   Exibição da probabilidade da previsão, dando um índice de confiança.
-   Modelo treinado com um dataset de URLs conhecidas, focado em características como comprimento e estrutura da URL.

## 🛠️ Tecnologias Utilizadas

-   **Python 3.13**
-   **Scikit-learn:** Para a construção e treinamento do modelo de Machine Learning.
-   **Pandas:** Para a manipulação e engenharia de características dos dados.
-   **Joblib:** Para salvar e carregar o modelo treinado.
-   **Jupyter Notebook:** Para a fase de exploração de dados e prototipagem do modelo.

## 🚀 Como Usar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/SEU-USUARIO/sentinel-ai.git
    cd sentinel-ai
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    python3 sentinel.py
    ```

## 🧠 Modelo de Machine Learning

O coração do SentinelAI é um classificador `RandomForestClassifier` da biblioteca Scikit-learn. O modelo foi treinado para identificar padrões em características extraídas das URLs, como:
-   Comprimento total da URL
-   Contagem de caracteres especiais ('.', '-', '/' )

O notebook de desenvolvimento (`Untitled.ipynb`) contém todo o processo de treinamento, desde a análise exploratória dos dados até a avaliação final do modelo.
