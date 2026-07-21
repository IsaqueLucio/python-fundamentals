"""
Projeto 1: Pipeline de Logs Resiliente
Pasta: 01_resilient_log_pipeline/
Arquivo Principal: main.py

Regras:
1. Crie um arquivo de log fictício chamado 'server_logs.txt' usando um Gerenciador de Contexto ("w").
   Escreva 100 linhas: a maioria formatada como "INFO:200:Success", algumas como "ERROR:500:Internal Fault",
   e insira intencionalmente 5 linhas corrompidas, como "INVALID_LINE_NO_DELIMITER" ou "INFO:INVALID_CODE:Test".

2. O Decorador: Crie um decorador '@execution_timer' que meça e exiba quanto tempo uma função leva para ser executada.

3. O Gerador (Leitor Preguiçoso): Crie uma função geradora 'stream_logs(file_path: str)'.
   - Use um bloco 'with open(file_path, "r")' dentro do gerador.
   - Percorra o arquivo linha por linha e use 'yield' para retornar cada linha sem os espaços em branco das extremidades.

4. O Processador (Tratamento de Erros): Crie uma função 'process_pipeline(file_path: str)' decorada com '@execution_timer'.
   - Itere sobre 'stream_logs(file_path)'.
   - Use um bloco 'try/except ValueError' para dividir cada linha usando dois-pontos (":").
   - Tente converter o elemento do meio (código de status) em um inteiro usando 'int(code)'.
   - Se uma linha estiver corrompida (IndexError ou ValueError), capture a exceção, imprima um aviso como "[SKIP] Linha de log malformada: ...", e continue o loop usando 'continue'.
   - Conte os logs válidos em duas categorias: 'success_count' e 'error_count', depois imprima o resumo final.
"""

from execution_time import execution_time

@execution_time
def process_pipeline(file_path: str):
    success_count = []
    error_count = []
    with open(file_path, "r") as file:
        for line in file:
            try:
                code = int(line.split(":")[1])
                success_count.append(code)
            except (ValueError, IndexError):
                print("[SKIP] Linha de log malformada: ...")
                error_count.append(line)
                continue
            finally:
                pass
    print(f"Number of successful logs: {len(success_count)}\nNumber of unsuccessful logs: {len(error_count)}")


