"""
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
"""

from retry_on_network_error import retry_on_network_error
from api_pages import get_pages

flag_page_2 = True
@retry_on_network_error
def fetch_page(page_number: int):
    global flag_page_2
    if page_number == 2 and flag_page_2:
        flag_page_2 = False
        raise ConnectionError("Network flicker!")
    elif page_number > 3:
        raise ValueError("Page not found (404)")
    else:
        return get_pages(page_number)