import google.generativeai as genai
import pdfplumber
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from scipy.spatial.distance import cosine
import numpy as np
from google.colab import userdata
# Carregar a chave da API Gemini (necessário para GenAI)
api_key = userdata.get('GEMINI_KEY')
genai.configure(api_key=api_key)  # Mantenha se quiser usar o GenAI

def preprocess_pdf(pdf_path):
    """
    Função para pré-processar o PDF.

    Args:
        pdf_path: Caminho para o arquivo PDF.

    Returns:
        str: Texto extraído do PDF.
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf = pdfplumber.open(pdf_file)
        pdf_text = ''
        for page in pdf.pages:
            pdf_text += page.extract_text()
    return pdf_text

def summarize_text(text, ratio=0.2):
    """
    Função para resumir o texto usando a biblioteca NLTK.

    Args:
        text: Texto a ser resumido.
        ratio: Razão de compressão do resumo (entre 0 e 1).

    Returns:
        str: Texto resumido.
    """
    # Download necessário apenas na primeira execução
    nltk.download('stopwords')
    nltk.download('punkt')

    stop_words = stopwords.words('portuguese')
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    sentences = sent_tokenize(text)

    sentence_vectors = []
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        sentence_vec = []
        for word in filtered_text:
            if word in sentence_words:
                sentence_vec.append(1)
            else:
                sentence_vec.append(0)
        sentence_vectors.append(sentence_vec)

    sentence_scores = np.apply_along_axis(lambda vec: cosine(vec, np.sum(sentence_vectors, axis=0)), axis=1, arr=np.array(sentence_vectors))
    top_sentences = np.argsort(sentence_scores)[:int(len(sentences) * ratio)]
    summary = ' '.join([sentences[idx] for idx in top_sentences])
    return summary

def chatbot_with_gemini(pdf_path, max_user_input_length=256):
    """
    Função principal para interagir com o chatbot Gemini.

    Args:
        pdf_path: Caminho para o arquivo PDF.
    """
    # Pré-processar o PDF
    preprocessed_text = preprocess_pdf(pdf_path)

    # Resumir o texto do PDF
    summary_text = summarize_text(preprocessed_text)

    # Iniciar a sessão de chat com o modelo Gemini
    chat = genai.GenerativeModel('gemini-pro').start_chat(history=[])

    # Enviar o prompt com o resumo do PDF como o texto inicial
    response = chat.send_message(summary_text)



    # Exibir o prompt inicial do chatbot
    print(f"Chatbot: {response.text}")
    # Perguntar ao usuário o que deseja saber sobre Finanças
    print("Chatbot: O que você deseja saber sobre Finanças? Vamos utilizar o PDF guia de finanças com estudos sobres os maiores especialistas em finanças de todos os tempos.")


    # Loop principal da conversa
    while True:
      # Obter a entrada do usuário
      user_input = input("Usuário: ")

      # Truncate user input if it exceeds the limit
      if len(user_input) > max_user_input_length:
        user_input = user_input[:max_user_input_length]

      # Processar a entrada do usuário e gerar uma resposta
      response = chat.send_message(user_input)

      # Exibir a resposta do chatbot
      print(f"Chatbot: {response.text}")

import requests

# URL do arquivo PDF no GitHub
pdf_url = "https://github.com/upcarreira/Meu-Portfolio/raw/main/Analise%20e%20Ciencia%20de%20Dados/ChatBot/guia-financas.pdf"

# Caminho onde o PDF será salvo localmente
pdf_local_path = "guia-financas.pdf"

# Baixar o PDF
response = requests.get(pdf_url)
with open(pdf_local_path, "wb") as pdf_file:
    pdf_file.write(response.content)

# Chamar a função chatbot_with_gemini() com o caminho local do PDF
chatbot_with_gemini(pdf_local_path)
