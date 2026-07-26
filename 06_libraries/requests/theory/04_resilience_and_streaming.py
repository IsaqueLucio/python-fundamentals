"""
Python Core - 06 Bibliotecas
Módulo: requests
Arquivo: 04_resilience_and_streaming.py
Descrição: Dominando tentativas automáticas com HTTPAdapters, tratamento de limites de requisição (rate limits) e download de grandes volumes de dados utilizando streams.
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os

print("--- 1. Construindo uma Sessão Resiliente (Tentativas Automáticas) ---")
# Em vez de escrever manualmente loops com try/except para repetir requisições
# quando um servidor falha, configuramos o mecanismo Retry do urllib3 e
# conectamos ele a uma Session do requests!

# Configura a estratégia de tentativas:
retry_strategy = Retry(
    total=3,  # Número máximo de tentativas adicionais
    backoff_factor=1,  # Tempo de espera: {fator de espera} * (2 ** ({número total de tentativas} - 1))
                       # -> 1s, 2s, 4s...
    status_forcelist=[429, 500, 502, 503, 504],  # Códigos HTTP que devem gerar uma nova tentativa automaticamente
    allowed_methods=["HEAD", "GET", "OPTIONS"]  # Apenas métodos HTTP seguros e idempotentes serão repetidos
)

# Cria um HTTPAdapter com essa estratégia:
adapter = HTTPAdapter(max_retries=retry_strategy)

# Conecta o adapter a uma nova Session para HTTP e HTTPS:
resilient_session = requests.Session()
resilient_session.mount("http://", adapter)
resilient_session.mount("https://", adapter)

url_unstable = "https://httpbin.org/status/503"  # Sempre retorna 503 Service Unavailable

print("Tentando acessar um endpoint instável (503). Observe o mecanismo repetir automaticamente...")
try:
    # Observe: chamamos .get() normalmente.
    # A Session + Adapter gerenciam automaticamente as esperas e novas tentativas!
    response = resilient_session.get(url_unstable, timeout=5)
    response.raise_for_status()

except requests.exceptions.RetryError as e:
    print(f"[RELATÓRIO DE RESILIÊNCIA] Número máximo de tentativas excedido! O servidor realmente está indisponível: {e}")

except requests.exceptions.RequestException as e:
    print(f"[ERRO DE REQUISIÇÃO] {e}")

resilient_session.close()

print("\n" + "="*60 + "\n")


print("--- 2. Streaming de Grandes Volumes de Dados (Download em Blocos) ---")
# Para baixar um arquivo grande sem consumir GBs de memória RAM, devemos utilizar:
# 'stream=True'.
# Isso impede o download imediato do corpo da resposta até que nós o percorramos
# explicitamente!

# Vamos baixar uma imagem de exemplo (ou um grande payload binário do httpbin):
url_big_data = "https://httpbin.org/bytes/50000"  # Gera um arquivo binário de 50.000 bytes

output_filepath = "streamed_backup.bin"

print("Iniciando download utilizando stream...")

try:
    # Observe:
    # stream=True informa ao requests:
    # "Baixe apenas os headers por enquanto!"
    with requests.get(url_big_data, stream=True, timeout=10) as stream_res:

        stream_res.raise_for_status()

        # Verifica o tamanho total do arquivo nos headers
        # (caso o servidor forneça essa informação):
        total_size = stream_res.headers.get('content-length')

        print(f"Tamanho informado pelo servidor: {total_size} bytes")

        # Abre o arquivo local no modo de escrita binária ('wb'):
        with open(output_filepath, "wb") as file:

            # Faz o download e salva em blocos de 8192 bytes (8 KB) por vez:
            for chunk in stream_res.iter_content(chunk_size=8192):

                if chunk:  # Ignora blocos vazios de keep-alive
                    file.write(chunk)

    print(
        f"[SUCCESS] Arquivo salvo com sucesso! "
        f"Tamanho no disco local: {os.path.getsize(output_filepath)} bytes."
    )

except requests.exceptions.RequestException as e:
    print(f"[ERRO DE STREAM] Falha ao baixar arquivo: {e}")

finally:
    # Remove o arquivo de teste criado no disco:
    if os.path.exists(output_filepath):
        os.remove(output_filepath)
        print("Arquivo de teste removido do disco.")