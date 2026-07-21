"""
Projeto 2: Paginador de API Robusto
Pasta: 02_robust_api_paginator/

Estrutura:
  - api_client.py (Simula o buscador de dados da rede)
  - main.py       (Consome os dados)

Regras:

1. No arquivo 'api_client.py':
   - Crie um decorator '@retry_on_network_error' que capture o erro
     ConnectionError e faça novas tentativas até 3 vezes antes de finalmente
     lançar a exceção novamente.
   - Crie uma função 'fetch_page(page_number: int)' decorada com '@retry'.
   - Simule que as páginas 1, 2 e 3 retornam listas de usuários:
     [{"id": 1, "name": "Alice"}, ...].
   - Se 'page_number == 2', intencionalmente lance
     ConnectionError("Network flicker!") na primeira tentativa para testar
     seu decorator de retry!
   - Se 'page_number > 3', lance:
     ValueError("Page not found (404)").

2. No arquivo 'main.py':
   - Importe 'fetch_page' do 'api_client'.
   - Crie um generator chamado 'get_all_users()'. Dentro de um loop infinito
     'while True:', tente buscar as páginas uma por uma.
   - Use 'yield from page_data' (ou faça um loop e use yield para cada usuário)
     para transmitir os usuários um por um.
   - Use 'try/except ValueError' dentro do generator:
     quando o erro 404 for capturado, interrompa o loop de forma limpa!
   - Itere sobre 'get_all_users()' usando um loop for e imprima cada usuário
     com segurança.
"""

from api_client import fetch_page
from api_pages import PAGES

def get_all_users():
   page = 1
   while True:
      try:
         page_data = fetch_page(page)
         yield from page_data
         page += 1
      except ValueError:
         break
      
for user in get_all_users():
   print(user)