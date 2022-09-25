from theory import theoretic_kintetic_energy, theoretic_mean_velocity, equation_of_state
from physics import PhysicsSimulation
from util import print_hash_line, plot_particles
from box import Box
import time 

def main():
    
    box = Box('dagaly')
    box.init_positions()
    box.init_velocities()

    # Calculate the kinetic energy in the box at its current state. 
    mean_KE = box.calcualte_mean_kinetic_energy()

    # Calculate the theoretical kinetic energy using the equation of 
    # and the temprature (T: Kelvin) of the box. 
    theoretic_KE = theoretic_kintetic_energy(box.T)

    print_hash_line("Kinetic energy", symbol="/")
    print("Numeric kinetic energy: {:.2e}".format(mean_KE))
    print("Theoretic kinetic energy: {:.2e}\n".format(theoretic_KE))
    
    # Calculate the relative error of the numerical calculation 
    relative_error = (theoretic_KE - mean_KE) / theoretic_KE
    print("Relative error: {:.2f}%".format((abs(relative_error)*100)))
    print_hash_line(symbol='=',newline=True)
    

    print_hash_line("Mean Velocity", symbol='/')
    # Theoretic mean velocity : sqrt(8*k*T /pi/m)
    theoretic_mean_v = theoretic_mean_velocity(box.T)
    # Numeric mean velocity at current state 
    mean_v = box.calculate_mean_velocity()

    print("Numeric mean velocity: {:.2f} m/s".format(mean_v))
    print("Theoretic mean velocity: {:.2f}m/s\n".format(theoretic_mean_v))

    # Relative error of mean velocity
    relative_error_v = (theoretic_mean_v - mean_v) / theoretic_mean_v
    print("Relative error {:.2f}%".format(abs(relative_error_v)*100))
    print_hash_line(symbol='=',newline=True)


    # Model physics 
    box.init_positions()
    box.init_velocities()
    model = PhysicsSimulation(box)

    # Run the simulation 
    print_hash_line("Physics simulation", symbol="/")
    start = time.time()
    model.run_model(data_capture=True) 
    print("Model time: ", time.time()-start )

    eq_of_state = equation_of_state(box.N, box.T, box.L)
    print("Equation of state: {:.2f}".format(eq_of_state) )

    p = model.momentum_count
    force = p / model.total_time 
    P = force / ( box.L**2 )
    print("Calculated pressure on the wall: {:.2f}\n".format(P))
    relative_error = (eq_of_state - P) / eq_of_state 
    print("Relative error: {:.2f}%".format(relative_error*100))
    print_hash_line(symbol='/')

    # Plotting 
    plot_particles()

    print("Debug")



if __name__ == "__main__":
    main()
