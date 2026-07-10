class SmartDevice:

    def __init__(self, name: str):
        self.name = name
        self.__is_on = False
    
    def turn_on(self) -> str:
        if self.__is_on == True:
            return f"{self.name} the device is already turned on."
        else:
            self.__is_on = True
            return f"{self.name} the device is now turned on."
    
    def turn_off(self):
        if self.__is_on == False:
            return f"{self.name} the device is already turned off."
        else:
            self.__is_on = False
            return f"{self.name} the device is now turned off."
    
    def is_active(self) -> bool:
        return True if self.__is_on == True else False

    
