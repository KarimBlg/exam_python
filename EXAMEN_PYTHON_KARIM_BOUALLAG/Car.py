from Vehicle import Vehicle

class Car(Vehicle):
    #attributs de classe 
    nom_car = ""
    #constructor
    def __init__(self, make, model, color, year):
        super().__init__(make, model, color)
        self.year = year
    
    #méthode afficher infos
    def Car_str(self):
        return f"Marque : {self.make}\nModele : {self.model}\nCouleur : {self.color}\nAnnée : {self.year}"
    
    #méthode récupérer type véhicule
    def get_vehicle_type(self):
        return "car"
    
    #getters
    def get_car_make(self):
        return f"{self.make}"
    
    def get_car_model(self):
        return f"{self.model}"
    
    def get_car_color(self):
        return f"{self.color}"
    
    def get_car_year(self):
        return f"{self.year}"
    
    #setters
    def set_car_make(self, make1):
        self.make = make1

    def set_car_model(self, model1):
        self.model = model1

    def set_car_color(self, color1):
        self.color = color1

    def set_car_year(self, year1):
        self.year = year1

Car1 = Car("mercedes", "e250", "grey", 2014)
Car2 = Car("audi", "a3", "black", 2017)
Car3 = Car("audi", "s3", "green", 2019)
Car4 = Car()
Car5 = Car()