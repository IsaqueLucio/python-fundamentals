from processor import Processor
from monitor import Monitor

class Computer:

    def __init__(self, cpu_model: str, cpu_cores: int):
        self.cpu_model = cpu_model
        self.cpu_cores = cpu_cores
        self.processor = Processor(cpu_model,cpu_cores)
        self.monitor = None
    
    def plug_monitor(self, monitor: Monitor):
        self.monitor = monitor

    def unplug_monitor(self):
        self.monitor = None
    
    def show_specs(self) -> str:
        there_monitor = ""
        if not self.monitor:
            there_monitor = "- No monitor connected."
        else:
            there_monitor = f"- Monitor: Brand = {self.monitor.get_brand()} | Resolution = {self.monitor.get_resolution()}"
        return f"--- Computer Specifications ---\n - Processor: Model = {self.processor.get_model()} | Cores = {self.processor.get_cores()}\n {there_monitor}"


    
