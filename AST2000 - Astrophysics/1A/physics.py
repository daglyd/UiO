
from concurrent.futures import thread
from tkinter import W
from box import Box
import numpy as np 
from tqdm import tqdm 
from multiprocessing import Process
from threading import Thread 
from numba import jit, njit 

class PhysicsSimulation:

    def __init__(self, box: Box, total_time=1e-9, n_steps=1000) -> None:
        
        self.total_time = total_time # Total time of simulation in seconds. 
        self.n_steps = n_steps # Number of time steps to simulate.
        self.time_step = self.total_time / self.n_steps 

        self.box = box 
        self.r = box.r 
        self.v = box.v 
        self.box_wall = self.box.L
        
        self.momentum_count = 0 


    def compute_timestep(self):

        self.r = self.r + (self.v * self.time_step)

        def turn_at_wall(i):
            wall_condition = np.where( (self.r[:,i] > self.box_wall) | (self.r[:,i] < 0))
            p = 2 * self.box.h_mass * abs(
                self.v[ 
                    np.where( self.r[:,i] > self.box_wall), i ] ).sum()
            self.v[wall_condition, i] = self.v[wall_condition, i] *-1

            return p  

        self.momentum_count += turn_at_wall(0)
        turn_at_wall(1)
        turn_at_wall(2)


        return self.r 
    
    def run_model(self, data_capture=False):
        if data_capture:
            file = open("data.csv", "w")
            file.write("t,x,y,z\n")
            for t in tqdm(range(self.n_steps)):
                r = self.compute_timestep()

                if t % 20 == 0:
                    r = np.insert(r, 0, t, axis=1)
                    np.savetxt(file, r, delimiter=",")
        else:
            for t in (range(self.n_steps)):
                self.compute_timestep()


        
    

