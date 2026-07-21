import json
import copy

class AtomicTransaction:

    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        with open(self.file_path, "r") as json_file:
            self.data = json.load(json_file)
            self.backup = copy.deepcopy(self.data)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"[ROLLBACK] Error detected ({exc_val}). Canceling all changes!")
            return True
        with open(self.file_path, "w") as json_file:
            json.dump(self.data, json_file, indent=4)
        print("[COMMIT] Transação salva com sucesso.")