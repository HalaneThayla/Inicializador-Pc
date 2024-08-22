import webbrowser
import time

# Lista de URLs para abrir
urls = [
    "https://www.google.com.br/?hl=pt-BR",
    "https://web.whatsapp.com",
    "https://www.google.com/intl/pt-BR/gmail/about/",
]

# Intervalo entre aberturas (em segundos)
delay = 5

# Função para abrir URLs
def open_urls(urls, delay):
    for url in urls:
        webbrowser.open(url)
        time.sleep(delay)

# Chama a função para abrir as URLs
open_urls(urls, delay)
