import numpy as np
import numpy as np 
from ast2000tools.solar_system import SolarSystem
from ast2000tools.utils import get_seed
import ast2000tools.constants as const


class Box:
    

    def __init__(self, seed_value):
        
        seed = get_seed(seed_value)
        system = SolarSystem(seed)
        home_planet_mass = system.masses[0] # Solar masses
        home_planet_mass_kg = home_planet_mass * const.m_sun # Solar masses -> kg 
        home_planet_radius = system.radii[0] * 1000 # km -> m

        G = const.G # Gravitational constant [m^3/kg/s^2]

        satellite_weight = 10000 # kg
        self.L = 1e-6 # Box Size
        self.T = 10000 # K : Temperature
        self.N =  1e5 # Number of particles in box: hydrogen molecules (H2)
        

        self.h2_mass = const.m_H2       # mass of hydrogen molecule [kg]
        self.h_mass = self.h2_mass / 2  # mass of hydrogen atom [kg]
        self.k = const.k_B
        v_esc = np.sqrt((2*G*home_planet_mass_kg)/
                        home_planet_radius) # m/s
        

    def init_positions(self):
        self.r = np.random.uniform(
                0,
                self.L,
                size=(int(self.N),3)
            )
        return None

    def init_velocities(self):
        self.v = np.random.normal(
                0,
                np.sqrt(1.38064852e-23*self.T/(const.m_H2/2)),
                size=(int(self.N),3)
            )
        return None

    def calculate_mean_velocity(self): 

        self.mean_v = np.linalg.norm(self.v, axis=1)
        self.mean_v = self.mean_v.mean() 
        return self.mean_v 


    def calcualte_mean_kinetic_energy(self):

        self.mean_energy = np.linalg.norm(self.v, axis=1)**2
        self.mean_energy = self.mean_energy.mean() 
        self.mean_energy = (1/2)*self.h_mass*self.mean_energy

        return self.mean_energy



