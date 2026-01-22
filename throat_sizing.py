import numpy as np
from rocketcea.cea_obj import CEA_Obj
import matplotlib.pyplot as plt

m_sq_to_in_sq = 1550 #1 m^2 = 1550 in^2


# This is a function that takes O/F ratio, chamber pressure (psia), 
# and thrust (N) as inputs, and outputs the diameter (in) of the throat 
def throat_sizing_function(of, pc, F, eps, pamb, gox_density, rp1_density, oxname, fuelname):
    # creates CEA object with Ox and Fuel
    cea_obj = CEA_Obj(oxName = oxname, fuelName = fuelname)
    # gets CEA list output
    output = cea_obj.get_PambCf(Pamb = 14.7, Pc = pc, MR = of, eps = 1)
    # get force coefficient
    cf = output[0]
    # get c* (need to convert ft/s to m/s)
    cstar = cea_obj.get_Cstar(Pc = pc, MR = of) * 0.3048 #m/s
    cstar = cstar * 0.8 # Efficiency factor
    # calculate isp
    isp = cea_obj.get_Throat_Isp(Pc=pc, MR=of, frozen=0)
    # get exhaust velocity
    v_e = isp * 9.80655 # m/s (assumed 90% of ideal) max - removed 0.9 , just including a
                        # general cstar efficiency
    # calculate mdot
    mdot = F/v_e #kg/s

    # mdot for gox and rp1 specifically
    gox_mdot = mdot * of /(1+of)
    rp1_mdot = mdot / (1+of)

    # convert pc to pascals
    pc_pa = 6894.76 * pc #Pa
    # calculate area of the throat (m^2)
    At = mdot * cstar/pc_pa
    # calculate diameter of throat (m)
    Dt_m = 2 * np.sqrt(At/np.pi)
    # convert to inches
    Dt_in = Dt_m / 0.3048 * 12
    
    T_c, T_t, T_e = cea_obj.get_Temperatures(Pc=pc, MR=of, eps = eps) #R

    T_ck = T_c * 5/9
    T_tk = T_t * 5/9
    T_ek = T_e * 5/9

    print("----------------------------------")
    print("Throat Sizing Parameters")
    print("----------------------------------")
    print(f"Throat Area (m^2): {At}")
    print(f"Throat Area (in^2): {At * m_sq_to_in_sq}")
    print(f"Throat Diameter (in): {Dt_in}")
    print("----------------------------------")
    print("Flow Parameters")
    print("----------------------------------")
    print(f"ISP (s): {isp}")
    print(f"C* (m/s): {cstar}")
    print(f"Exhaust Velocity (m/s): {v_e}")
    print(f"M Dot (kg/s): {mdot}")
    print(f"GOX M Dot (kg/s): {gox_mdot}")
    print(f"RP1 M Dot (kg/s): {rp1_mdot}")
    print(f"GOX Volumetric Flow Rate (m^3/s): {gox_mdot/gox_density}")
    print(f"GOX Volumetric Flow Rate (in^3/s): {61020 * gox_mdot/gox_density}")
    print(f"RP1 Volumetric Flow Rate (m^3/s): {rp1_mdot/rp1_density}")
    print(f"RP1 Volumetric Flow Rate (in^3/s): {61020 * rp1_mdot/rp1_density}")
    print("----------------------------------")
    print("Temperature Parameters")
    print("----------------------------------")
    print(f"Combustion Temperature (K): {T_ck}")
    print(f"Throat Temperature (K): {T_tk}")
    print(f"Exhaust Temperature (K): {T_ek}")
    print("----------------------------------")

    return(At * m_sq_to_in_sq, mdot, Dt_in)