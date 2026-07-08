class Processor:

    def __init__(self, model: str, cores: int):
        self.model = model
        self.cores = cores
    
    def get_model(self) -> str:
        return self.model
    
    def get_cores(self) -> int:
        return self.cores