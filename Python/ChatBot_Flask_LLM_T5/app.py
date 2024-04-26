import json
import os
from flask import Flask, render_template, request
import requests
from difflib import SequenceMatcher

app = Flask(__name__)

MIN_SIMILARITY_THRESHOLD = 0.5

# Carregar o arquivo JSON com os dados pré-processados
preprocessed_json_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dados_preprocessados.json')
with open(preprocessed_json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    training_data = data['training_data']

# Lista para armazenar a memória do chatbot
memory = []

def generate_answer(question):
    payload = {
        "inputs": question,
        "options": {
            "use_cache": True,
            "max_length": 1024
        }
    }
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    response = requests.post("https://api-inference.huggingface.co/models/google/flan-t5-xxl", headers=headers, json=payload)
    response_json = response.json()
    if 'generated_text' in response_json:
        return response_json['generated_text'][:1024]  # Limitar a resposta a 1024 caracteres
    else:
        return None


# Função para calcular a similaridade entre duas strings
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Função para consultar a memória do chatbot
def query_memory(question):
    max_similarity = 0
    best_match = None

    for item in memory:
        pergunta_memoria = item['question']
        resposta_memoria = item['answer']
        similarity = similar(question, pergunta_memoria)

        if similarity > max_similarity:
            max_similarity = similarity
            if similarity >= MIN_SIMILARITY_THRESHOLD:
                best_match = resposta_memoria
            else:
                best_match = None

    return best_match

# Função para consultar os dados pré-processados e obter a resposta adequada
def query_data(question):
    max_similarity = 0
    best_match = None

    for item in training_data:
        pergunta = item['pergunta']
        resposta = item['resposta']
        similarity = similar(question, pergunta)

        if similarity > max_similarity:
            max_similarity = similarity
            if similarity >= MIN_SIMILARITY_THRESHOLD:
                best_match = resposta
            else:
                best_match = None

    return best_match

# Rota principal para exibir o formulário
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Rota para lidar com as solicitações POST do formulário
@app.route('/chat', methods=['POST'])
def chat():
    pergunta = request.json['question']
    resposta_memoria = query_memory(pergunta)

    if resposta_memoria is not None:
        return resposta_memoria[:1024]  # Limitar a resposta a 1024 caracteres

    resposta = query_data(pergunta)

    if resposta is not None:
        resposta_api = generate_answer(pergunta)

        if resposta_api:
            similarity = similar(resposta, resposta_api)

            if similarity > 0.8:
                return resposta[:1024]  # Limitar a resposta a 1024 caracteres
            else:
                return resposta_api[:1024]  # Limitar a resposta da API a 1024 caracteres
        else:
            return resposta[:1024]  # Limitar a resposta a 1024 caracteres
    else:
        resposta = generate_answer(pergunta)
        if resposta:
            return resposta[:1024]  # Limitar a resposta a 1024 caracteres
        else:
            return "Desculpe, não tenho uma resposta para essa pergunta."

# Rota para adicionar perguntas e respostas à memória
@app.route('/add_memory', methods=['POST'])
def add_memory():
    pergunta = request.json['question']
    resposta = request.json['answer']

    memory.append({'question': pergunta, 'answer': resposta})

    return "Memória atualizada com sucesso!"

# Rota para exibir a memória
@app.route('/memory', methods=['GET'])
def show_memory():
    return json.dumps(memory)

if __name__ == '__main__':
    app.run(debug=True)
