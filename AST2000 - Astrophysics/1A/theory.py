import numpy as np 
import ast2000tools.constants as const


def theoretic_kintetic_energy(T):
    return (3/2)*const.k_B*T 


def theoretic_mean_velocity(T):
    mean_v = np.sqrt(
        ( 8*const.k_B*T) /
        ( np.pi * const.m_H2/2)
    )
    return mean_v

def equation_of_state(n, T, L):
    return (n/L**3)*const.k_B*T