class Vehicle:
    #attributs de classe 
    nom_vehicle = ""

    #constructor
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    
    #getters
    def get_vehicle_make(self):
        return f"{self.make}"
    
    def get_vehicle_model(self):
        return f"{self.model}"
    
    def get_vehicle_color(self):
        return f"{self.color}"
    
    
    #setters
    def set_vehicle_make(self, make1):
        self.make = make1

    def set_vehicle_model(self, model1):
        self.model = model1

    def set_vehicle_color(self, color1):
        self.color = color1
