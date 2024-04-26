import json
import os
import nltk
from nltk.corpus import stopwords
import string

# Baixar o pacote de stopwords em português
nltk.download('stopwords')

# Caminho para o arquivo JSON com as perguntas e respostas
json_path = os.path.join(os.path.dirname(__file__), 'dados.json')

# Carregar o arquivo JSON com as perguntas e respostas
with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Pré-processamento dos dados
training_data = []
stopwords_set = set(stopwords.words('portuguese'))

for item in data:
    pergunta = item['pergunta']
    resposta = item['resposta']

    # Tokenização
    pergunta_tokens = nltk.word_tokenize(pergunta.lower())
    resposta_tokens = resposta.lower().split()  # Utilizando split para preservar as vírgulas

    # Limite de tokens para 1024
    pergunta_tokens = pergunta_tokens[:1024]
    resposta_tokens = resposta_tokens[:1024]

    # Reconstituir as perguntas e respostas pré-processadas
    pergunta_preprocessada = ' '.join(pergunta_tokens)
    resposta_preprocessada = ' '.join(resposta_tokens)

    # Formate a pergunta e resposta em um único dicionário no formato desejado
    item_preprocessado = {
        'pergunta': pergunta_preprocessada,
        'resposta': resposta_preprocessada
    }
    training_data.append(item_preprocessado)

# Salvar os dados pré-processados em um arquivo JSON
dados_preprocessados = {
    'training_data': training_data
}
preprocessed_json_path = os.path.join(os.path.dirname(__file__), 'dados_preprocessados.json')
with open(preprocessed_json_path, 'w', encoding='utf-8') as file:
    json.dump(dados_preprocessados, file, ensure_ascii=False, indent=4)
