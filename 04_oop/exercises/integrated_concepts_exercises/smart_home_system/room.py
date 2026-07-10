from device import SmartDevice

class Room:

    def __init__(self, name: str):
        self.name = name
        self.devices = []

    def add_device(self, device: SmartDevice):
        self.devices.append(device)

    def turn_on_all(self) -> str:
        messages = []
        for device in self.devices:
            messages.append(device.turn_on())
        return "\n".join(messages)  
    