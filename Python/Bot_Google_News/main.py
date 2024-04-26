from GoogleNews import GoogleNews
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Função para realizar a busca por notícias no Google News
def search_news(query, num_results=7, lang="pt-BR"):
    googlenews = GoogleNews(lang=lang)
    googlenews.search(query)
    news_results = googlenews.results()[:num_results]
    return news_results

# Realizando a busca por notícias no Google News
query = "IA"
news_results = search_news(query, num_results=7, lang="pt-BR")

# Exibindo os resultados
for i, news in enumerate(news_results, start=1):
    print(f"Notícia {i}: {news['title']}")
    print(f"Descrição: {news['desc']}")
    print(f"Link: {news['link']}")
    print()

def enviar_email(noticias):
    # Configurações do email
    email_from = "upcarreiraclaudio@gmail.com"
    email_to = "upcarreiraclaudio@gmail.com"
    senha = "pydiznhlundtzcph"  # Insira sua senha aqui

    # Criando a mensagem de email
    msg = MIMEMultipart()
    msg["From"] = email_from
    msg["To"] = email_to
    msg["Subject"] = "Notícias sobre IA"

    # Construindo o corpo do email com as notícias
    body = ""
    for i, noticia in enumerate(noticias, start=1):
        body += f"Notícia {i}: {noticia['title']}\n"
        body += f"Descrição: {noticia['desc']}\n"
        body += f"Link: {noticia['link']}\n\n"

    msg.attach(MIMEText(body, "plain"))

    # Enviando o email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_from, senha)
    server.send_message(msg)
    server.quit()

# Chamada da função para enviar as notícias por email
enviar_email(news_results)
