"""
Python Core - 06 Bibliotecas
Módulo: requests
Arquivo: 05_mutating_data.py
Descrição: Dominando operações CRUD RESTful (POST, PUT, PATCH, DELETE) e uploads de arquivos multipart.
"""
import requests
import os

# Usamos o JSONPlaceholder, a API falsa gratuita padrão da indústria para testar operações CRUD RESTful:
BASE_URL = "https://jsonplaceholder.typicode.com"

print("--- 1. CREATE: Enviando cargas JSON com POST ---")
# Para criar um novo recurso, enviamos uma requisição POST com um dicionário
# passado para o parâmetro 'json='.
new_post_payload = {
    "title": "Python Core Deep Dive",
    "body": "Dominando mutações HTTP e arquiteturas RESTful.",
    "userId": 101
}

try:
    res_post = requests.post(f"{BASE_URL}/posts", json=new_post_payload, timeout=5)
    res_post.raise_for_status()

    # 201 Created é o código de status HTTP padrão para criação bem-sucedida de um recurso!
    print(f"Código de Status: {res_post.status_code} (Criado)")
    print("Resposta do servidor (com ID gerado):")
    print(res_post.json())
except requests.exceptions.RequestException as e:
    print(f"[ERRO POST] {e}")

print("\n" + "=" * 60 + "\n")

print("--- 2. UPDATE: Substituição Completa (PUT) vs Modificação Parcial (PATCH) ---")
# Vamos usar como alvo um recurso existente: Post ID 1
target_url = f"{BASE_URL}/posts/1"

# PUT substitui o recurso INTEIRO.
# Se você omitir um campo, ele pode ser sobrescrito como nulo!
put_payload = {
    "id": 1,
    "title": "Título Completamente Substituído",
    "body": "Conteúdo do corpo completamente substituído.",
    "userId": 1
}

res_put = requests.put(target_url, json=put_payload, timeout=5)
print(f"PUT - Código de Status: {res_put.status_code} (OK)")
print(f"PUT - Título Resultante: {res_put.json()['title']}")

# PATCH modifica APENAS os campos enviados,
# mantendo o restante do recurso intacto!
patch_payload = {
    "title": "Apenas o Título Foi Atualizado"
}

res_patch = requests.patch(target_url, json=patch_payload, timeout=5)
print(f"\nPATCH - Código de Status: {res_patch.status_code} (OK)")
print(f"PATCH - Título Resultante: {res_patch.json()['title']}")

print("\n" + "=" * 60 + "\n")


print("--- 3. DELETE: Removendo Recursos com Segurança ---")
# DELETE remove o recurso do servidor.
try:
    res_delete = requests.delete(target_url, timeout=5)
    res_delete.raise_for_status()

    # Muitas APIs REST retornam 200 OK (com JSON vazio)
    # ou 204 No Content (sem corpo na resposta).
    print(f"DELETE - Código de Status: {res_delete.status_code}")
    print("Recurso removido com sucesso do servidor!")
except requests.exceptions.RequestException as e:
    print(f"[ERRO DELETE] {e}")

print("\n" + "=" * 60 + "\n")


print("--- 4. UPLOAD MULTIPART: Enviando Arquivos Físicos ---")
# Para enviar arquivos, usamos o parâmetro 'files='.
# Utilizaremos httpbin.org/post, que devolve os arquivos recebidos!
url_upload = "https://httpbin.org/post"
test_filename = "sample_upload.txt"

# Cria um arquivo temporário local para envio:
with open(test_filename, "w", encoding="utf-8") as f:
    f.write("Este é um arquivo de teste para upload multipart no Python Core!")

try:
    # Sintaxe: files = {"nome_do_campo": open("caminho_do_arquivo", "modo")}
    # Observação: Sempre abra arquivos em modo de leitura binária ('rb')
    # ao enviá-los via HTTP!
    with open(test_filename, "rb") as file_to_upload:
        files_payload = {"attachment": file_to_upload}

        # Também podemos enviar dados de formulário juntamente com o arquivo usando 'data='!
        form_data = {
            "user": "Isaque",
            "description": "Relatório semanal de atividades"
        }

        res_upload = requests.post(
            url_upload,
            files=files_payload,
            data=form_data,
            timeout=10
        )
        
        res_upload.raise_for_status()

        print("Upload realizado com sucesso! O que o servidor recebeu:")
        response_data = res_upload.json()
        print(f"Dados do formulário recebidos: {response_data['form']}")
        print(f"Conteúdo do arquivo recebido: {response_data['files']['attachment']}")

except requests.exceptions.RequestException as e:
    print(f"[ERRO UPLOAD] {e}")

finally:
    # Remove o arquivo local temporário:
    if os.path.exists(test_filename):
        os.remove(test_filename)
        print("\nArquivo temporário de upload removido do disco.")