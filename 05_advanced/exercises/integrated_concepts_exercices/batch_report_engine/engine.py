import csv
import os
from datetime import datetime
from utils.decorators import audit_log
import json

class Engine:

    def __init__(self):
        self.file_name = f"transactions_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.csv"
        self.file = self.create_file()
        self.num_transactions = 0

    def create_file(self):
        file_path = os.path.join(os.path.dirname(__file__), self.file_name)
        with open(file_path, "w") as file:
            pass
        return file_path
    
    def insert_transactions(self, value: float):
        if self.num_transactions == 0:
            self.num_transactions += 1
            with open(self.file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["id", "value"])
                writer.writerow([self.num_transactions, value])
        else:
            self.num_transactions += 1
            with open(self.file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self.num_transactions, value])
    
    def read_transactions(self):
        with open(self.file,"r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                yield row

    def read_transactions_values(self):
        with open(self.file,"r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                yield row[1]
    
    def filter_valid_transactions(self):
        for val in self.read_transactions_values():
            try:
                valid_val = float(val)
                if valid_val > 0:
                    yield valid_val
            except ValueError:
                pass

    @audit_log("REPORT_GENERATION")
    def generate_summary_report(self):
        cont = 0
        total = 0
        media = 0
        for val in self.filter_valid_transactions():
            cont += 1
            total += val
            media = total/cont
        final_json = {
            "file_information": self.file_name,
            "total_revenue": total,
            "average_transaction": media,
            "valid_transactions_count": cont
        }
        json_file_name = f"report_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.json"
        json_path = os.path.join(os.path.dirname(__file__), json_file_name)
        with open(json_path, "w") as json_file:
            json.dump(final_json, json_file, indent=4)
        return json_path