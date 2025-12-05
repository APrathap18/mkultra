import numpy as np
from rocketcea.cea_obj import CEA_Obj
import matplotlib.pyplot as plt
import throat_sizing
import plot_OF
import TTP_Orifice
#import TTP Orifice

oxName = 'GOX'
fuelName = 'RP1'
pamb = 14.7 # psia
g = 1.26 #ox
rhoRP1 = 810 #kg/m^3
rhoGOX = 1.429 #kg/m^3, 8.9497e-1
L_star = 45 #in

def main():
    of = 1.4
    pc = 150 # psia
    F = 15 # N
    d_c = 1.5 # in
    p1 = 300 # psia
    num_rp1_orifice = 4 
    num_gox_orifice = 4
    eps = 1

    [At_in, m_dot] = throat_sizing.throat_sizing_function(of, pc, F, eps, pamb, rhoGOX, rhoRP1, oxName, fuelName) # in^2

    # EPS of 1 because no diverging section
    plot_OF.plot_OF(pc, 1, oxName, fuelName, pamb)

    TTP_Orifice.orifice_area(At_in, of, pc, m_dot, d_c, p1, num_rp1_orifice, num_gox_orifice, rhoRP1, rhoGOX, L_star, g)
    #print(Dt_in)

if __name__ == "__main__":
    main()