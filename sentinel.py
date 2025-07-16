import joblib
import pandas as pd

def extract_features(url):
    """Extrai as mesmas características que usamos no treinamento."""
    features = {}
    features['url_length'] = len(url)
    features['dot_count'] = url.count('.')
    features['hyphen_count'] = url.count('-')
    features['slash_count'] = url.count('/')
    
    # Retorna os dados no formato de DataFrame que o modelo espera
    return pd.DataFrame([features])

# 1. Carregar o modelo treinado
print("Carregando o modelo SentinelAI...")
model = joblib.load('sentinel_model.pkl')
print("Modelo carregado com sucesso.\n")

# 2. Loop infinito para testar várias URLs
while True:
    # 3. Pedir uma URL ao usuário
    user_url = input("Digite a URL que deseja verificar (ou 'sair' para fechar): ")

    # 4. Condição de saída
    if user_url.lower() == 'sair':
        break

    # 5. Extrair as características da URL do usuário
    url_features = extract_features(user_url)

    # 6. Fazer a previsão
    prediction = model.predict(url_features)
    prediction_proba = model.predict_proba(url_features)

    # 7. Exibir o resultado
    print(f"\nAnalisando a URL: {user_url}")
    print(f"Previsão do modelo: {prediction[0].upper()}")
    
    # Imprime a probabilidade de forma mais clara
    if prediction[0] == 'bad':
        print(f"Probabilidade de ser maliciosa: {prediction_proba[0][0]:.2%}")
    else:
        print(f"Probabilidade de ser benigna: {prediction_proba[0][1]:.2%}")
    
    print("-" * 30)

print("\nSentinelAI finalizado.")
