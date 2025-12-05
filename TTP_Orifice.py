import numpy as np
import math as math
from rocketcea.cea_obj import CEA_Obj
import matplotlib.pyplot as plt

def orifice_area(A_t, of, pc, mdot, d_c, p1, num_rp1_orifice, num_gox_orifice, rhoRP1, rhoGOX, L_star, g):
    #RP-1, incompressible flow
    orifice_rp1 = mdot/(of * math.sqrt(2*rhoRP1*(p1 - pc))) # finds orifice area of RP1 in m^2

    print("Chamber Sizing Parameters")
    print("----------------------------------")

    print(f"L* for GOX/RP1: {L_star} in")

    V_c = A_t * L_star #in^3

    print(f"Chamber Volume: {V_c} in^3")
    print(f"Chamber Diameter: {d_c} in")

    A_c = math.pi * d_c**2 / 4

    print(f"Chamber Area: {A_c} in^2")

    L_c = V_c/(1.1 * A_c)

    print(f"Chamber Length: {L_c} in")

    print("----------------------------------")

    print("Orifice Sizing Parameters")
    print("----------------------------------")
    print(f"RP1 Orifice Count: {num_rp1_orifice}")
    print(f"RP1 Orifice Area: {orifice_rp1/10**-6} mm^2")  #output in mm^2
    print(f"RP1 Orifice Area (TOTAL, assuming square): {orifice_rp1*1550} in^2") # output in in^2 
    print(f"RP1 Orifice Area (per orifice): {orifice_rp1*1550/num_rp1_orifice} in")
    print(f"RP1 Orifice Diameter (per orifice): {math.sqrt(orifice_rp1*1550/num_rp1_orifice)} in")

    #GOX, compressible flow
    #mdot = Cd*A * sqrt(g*dens*P0((2/g+1))^((g+1)/(g-1))) #compressible, kg/s
    orifice_gox = mdot*of/(math.sqrt(g*rhoGOX*p1*((2/g+1))**((g+1)/(g-1))))
    print(f"GOX Orifice Count: {num_gox_orifice}")
    print(f"GOX Orifice Area: {orifice_gox/10**-6} mm^2")  #output in mm^2
    print(f"GOX Orifice Area (TOTAL, assuming circle): {orifice_gox*1550} in^2") # output in in^2 
    print(f"GOX Orifice Area (per orifice): {orifice_gox*1550 / num_gox_orifice} in^2") # output in in^2 
    print(f"GOX Orifice Diameter (per orifice): {2 * math.sqrt((orifice_gox*1550 / num_gox_orifice) / math.pi)} in")
    print("----------------------------------")
