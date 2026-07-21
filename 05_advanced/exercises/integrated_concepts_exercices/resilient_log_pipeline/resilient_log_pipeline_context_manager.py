import os
from execution_time import execution_time

class Log:
    def __init__(self, file_name: str):
        self.filename_path = os.path.join(os.path.dirname(__file__), file_name)

    @execution_time
    def log_creator(self):
        with open(self.filename_path, "w") as file:
            for i in range(100):
                if i in [2, 20, 71]:
                    file.write("INVALID_LINE_NO_DELIMITER\n")
                elif i in [35, 99]:
                    file.write("INFO:INVALID_CODE:Test\n")
                elif i in [23, 60, 33, 40, 81, 90]:
                    file.write("ERROR:500:Internal Fault\n")
                else:
                    file.write("INFO:200:Success\n")

    def stream_logs(self):
        with open(self.filename_path, "r") as file:
            for line in file:
                yield line.strip()
    
    def get_filename_path(self):
        return self.filename_path


