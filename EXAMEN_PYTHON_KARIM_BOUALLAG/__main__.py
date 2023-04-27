import sys
import tkinter as tk
from tkinter import messagebox
from Vehicle import Vehicle
from Car import Car
from Motor import Motor


class VehicleApp:
    #constructor
    def __init__(self, master):
        self.master = master
        self.master.title("Application de gestion de véhicules (Karim BOUALLAG)")
        
        self.vehicles = []
        
        # Créer les widgets pour l'interface graphique
        tk.Label(self.master, text="Type de véhicule:").grid(row=0, column=0)
        self.vehicle_type_entry = tk.Entry(self.master)
        self.vehicle_type_entry.grid(row=0, column=1)
        
        tk.Label(self.master, text="Marque:").grid(row=1, column=0)
        self.make_entry = tk.Entry(self.master)
        self.make_entry.grid(row=1, column=1)
        
        tk.Label(self.master, text="Modèle:").grid(row=2, column=0)
        self.model_entry = tk.Entry(self.master)
        self.model_entry.grid(row=2, column=1)
        
        tk.Label(self.master, text="Couleur:").grid(row=3, column=0)
        self.color_entry = tk.Entry(self.master)
        self.color_entry.grid(row=3, column=1)
        
        tk.Label(self.master, text="Année(Voiture):").grid(row=4, column=0)
        self.year_entry = tk.Entry(self.master)
        self.year_entry.grid(row=4, column=1)
        
        tk.Label(self.master, text="Taille du moteur(Moto):").grid(row=5, column=0)
        self.engine_size_entry = tk.Entry(self.master)
        self.engine_size_entry.grid(row=5, column=1)
        
        self.add_button = tk.Button(self.master, text="Ajouter", command=self.add_vehicle)
        self.add_button.grid(row=6, column=0)
        
        self.remove_button = tk.Button(self.master, text="Supprimer", command=self.delete_vehicle)
        self.remove_button.grid(row=6, column=1)
        
        self.stats_button = tk.Button(self.master, text="Statistiques", command=self.generate_statistics)
        self.stats_button.grid(row=7, column=0)
        
        self.stats_type_button = tk.Button(self.master, text="Statistiques par type", command=self.generate_statistics_by_type)
        self.stats_type_button.grid(row=7, column=1)
        
        self.stats_color_button = tk.Button(self.master, text="Statistiques par couleur", command=self.generate_statistics_by_color)
        self.stats_color_button.grid(row=7, column=2)
        
        self.vehicle_listbox = tk.Listbox(self.master)
        self.vehicle_listbox.grid(row=8, column=0, columnspan=3)

        self.quit_button = tk.Button(self.master, text="Quitter l'application", command=self.quit_app)
        self.quit_button.grid(row=9, column=3)
        
    #méthode ajouter véhicule
    def add_vehicle(self):
        vehicle_type = self.vehicle_type_entry.get()
        make = self.make_entry.get()
        model = self.model_entry.get()
        color = self.color_entry.get()
        
        
        if vehicle_type == "car":
            year = self.year_entry.get()
            vehicle = Car(make, model, color, year)
        elif vehicle_type == "motor":
            engine_size = self.engine_size_entry.get()
            vehicle = Motor(make, model, color, engine_size)
            
        self.vehicles.append(vehicle)
        self.vehicle_listbox.insert(tk.END, vehicle)
        self.vehicle_type_entry.delete(0, tk.END)
        self.make_entry.delete(0, tk.END)
        self.model_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.engine_size_entry.delete(0, tk.END)
        

    #méthode supprimer véhicule
    def delete_vehicle(self):
        selection = self.vehicle_listbox.curselection()
        for vehicle_index in selection[::-1]:
            self.vehicles.pop(vehicle_index)
            self.vehicle_listbox.delete(vehicle_index)
    
    #méthode statistiques
    def generate_statistics(self):
        num_vehicles = len(self.vehicles)
        num_cars = len([v for v in self.vehicles if isinstance(v, Car)])
        num_motorcycles = len([v for v in self.vehicles if isinstance(v, Motor)])
        
        tk.messagebox.showinfo("Statistiques générales", f"Nombre total de véhicules: {num_vehicles}\nNombre de voitures: {num_cars}\nNombre de motos: {num_motorcycles}")
    
    #méthode statistiques par type
    def generate_statistics_by_type(self):
        num_cars = len([v for v in self.vehicles if isinstance(v, Car)])
        num_motorcycles = len([v for v in self.vehicles if isinstance(v, Motor)])
        
        
        tk.messagebox.showinfo("Statistiques par type de véhicule", f"Nombre de voitures: {num_cars}\nNombre de motos: {num_motorcycles}")
    
    #méthode statistiques par couleur
    def generate_statistics_by_color(self):
        colors = {}
        for vehicle in self.vehicles:
            if vehicle.color not in colors:
                colors[vehicle.color] = 1
            else:
                colors[vehicle.color] += 1
        
        stats_str = "Statistiques par couleur:\n"
        for color, count in colors.items():
            stats_str += f"{color}: {count}\n"
        
        
        tk.messagebox.showinfo("Statistiques par couleur", stats_str)

    #méthode quitter l'application
    def quit_app(self):
        sys.exit()

#lancer l'application
root = tk.Tk()
app = VehicleApp(root)
root.mainloop()
