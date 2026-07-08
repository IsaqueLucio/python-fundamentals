class Monitor:

    def __init__(self, brand: str, resolution: str):
        self.brand = brand
        self.resolution = resolution

    def get_brand(self) -> str:
        return self.brand
    
    def get_resolution(self) -> str:
        return self.resolution