class Person:
    def __init__(self, addr, client):
        self.addr = addr  # IP address
        self.client = client  # socket client
        self.name = None  # name

    def set_name(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.addr}, {self.name})"