from Vehicle import Vehicle

class Motor(Vehicle):
    #attributs de classe 
    nom_motor = ""
    #constructor
    def __init__(self, make, model, color, engine_size):
        #attributs d'instance avec héritage
        super().__init__(make, model, color)
        self.engine_size = engine_size
    #méthode afficher infos
    def Car_str(self):
        return f"Marque : {self.make}\nModele : {self.model}\nCouleur : {self.color}\nTaille du moteur : {self.engine_size}"
    #méthode récupérer type véhicule
    def get_vehicle_type(self):
        return "motorcycle"
    
    #getters
    def get_motor_make(self):
        return f"{self.make}"
    
    def get_motor_model(self):
        return f"{self.model}"
    
    def get_motor_color(self):
        return f"{self.color}"
    
    def get_motor_engine_size(self):
        return f"{self.engine_size}"
    
    #setters
    def set_motor_make(self, make1):
        self.make = make1

    def set_motor_model(self, model1):
        self.model = model1

    def set_motor_color(self, color1):
        self.color = color1

    def set_motor_enginesize(self, enginesize1):
        self.engine_size = enginesize1

motor1 = Motor("kawazaki", "z1000", "black", 1000)
motor2 = Motor("keeway", "k150", "blue", 200)
motor3 = Motor("honda", "h12", "red", 350)
motor4 = Motor()
motor5 = Motor()