"""
Project 4: The Ultimate Batch Report Engine
Folder: 04_batch_report_engine/
Structure:
  - utils/
      - __init__.py
      - decorators.py (Contains @audit_log)
  - engine.py         (Contains the Generator pipeline and file processing)
  - main.py           (Runs the application)

Rules:
1. In 'decorators.py': Create '@audit_log(operation_name)' (a decorator that accepts arguments!). It should print a log before and after the wrapped function runs, recording the timestamp.

2. In 'engine.py':
   - Create a generator 'read_transactions(file_path)' that streams lines from a raw CSV/text file using a Context Manager ("r").
   - Create a chained generator 'filter_valid_transactions(raw_gen)' that yields only positive transaction amounts, catching and discarding invalid formats (like letters) using 'try/except'.
   - Create a function 'generate_summary_report(file_path)' decorated with '@audit_log("REPORT_GENERATION")'. It should consume the generator pipeline, calculate total revenue and average transaction value, and save the result into 'report.json' using a Context Manager ("w").

3. In 'main.py':
   - Create a dummy 'transactions.csv' with 50 lines of numbers, negative numbers, and random text errors.
   - Call 'generate_summary_report("transactions.csv")'.
   - Open 'report.json' at the end and print the finalized financial metrics!
"""

from engine import Engine
import json
import random


def main():
    engine = Engine()

    # Criando 50 transações fictícias
    values = [
        100,
        250,
        -50,
        300,
        "erro",
        "abc",
        500,
        -20
    ]

    for _ in range(50):
        value = random.choice(values)
        engine.insert_transactions(value)

    # Gerando relatório
    engine.generate_summary_report()

    # Procurando o relatório gerado
    print("\nRelatório gerado com sucesso!")

    print("\nArquivo de transações:")
    print(engine.file)

    print("\nAbrindo relatório:")

    # Como seu generate_summary_report cria o arquivo dinamicamente,
    # vamos procurar o JSON na pasta
    import os

    for file in os.listdir(os.path.dirname(__file__)):
        if file.startswith("report_") and file.endswith(".json"):
            report_path = os.path.join(os.path.dirname(__file__), file)

            with open(report_path, "r") as json_file:
                report = json.load(json_file)

            print(json.dumps(report, indent=4))
            break


if __name__ == "__main__":
    main()

