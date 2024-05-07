class Auto:
    def __init__(self, znacka, model, motor):
        self.znacka = znacka
        self.model = model
        self.motor = motor

class AutoBuilder:
    def __init__(self):
        self.znacka = None
        self.motor = None
        self.model = None

    def nastav_znacku(self, znacka):
        self.znacka = znacka
        return self

    def nastav_model(self, model):
        self.model = model
        return self

    def nastav_motor(self, motor):
        self.motor = motor
        return self


    def build(self):
        return Auto(self.znacka, self.model, self.motor)


builder = AutoBuilder()
auto = (builder.nastav_znacku("Skoda")
             .nastav_model("Octavia")
             .nastav_motor("1.6 TDI")
             .build())

print(auto.znacka, auto.model, auto.motor)