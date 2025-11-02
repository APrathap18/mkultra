import numpy as np
from rocketcea.cea_obj import CEA_Obj
import matplotlib.pyplot as plt
oxName = 'GOX'
fuelName = 'RP1'
pamb = 14.7 # psia

# This is a function that takes O/F ratio, chamber pressure (psia), 
# and thrust (N) as inputs, and outputs the diameter (in) of the throat 
def throat_sizing_function(of, pc, F):
    # creates CEA object with Ox and Fuel
    cea_obj = CEA_Obj(oxName = 'GOX', fuelName = 'RP1')
    # gets CEA list output
    output = cea_obj.get_PambCf(Pamb = 14.7, Pc = pc, MR = of, eps = 1)
    # get force coefficient
    cf = output[0]
    # get c* (need to convert ft/s to m/s)
    cstar = cea_obj.get_Cstar(Pc = pc, MR = of) * 0.3048 #m/s
    # calculate isp
    isp = cstar * cf #s
    # get exhaust velocity
    v_e = 0.9 * isp # m/s (assumed 90% of ideal)
    # calculate mdot
    mdot = F/v_e #kg/s
    # convert pc to pascals
    pc_pa = 6894.76 * pc #Pa
    # calculate area of the throat (m^2)
    At = mdot * cstar/pc_pa
    # calculate diameter of throat (m)
    Dt_m = 2 * np.sqrt(At/np.pi)
    # convert to inches
    Dt_in = Dt_m / 0.3048 * 12

    print("----------------------------------")
    print(f"ISP (s): {isp}")
    print(f"C* (m/s): {cstar}")
    print(f"Exhaust Velocity (m/s): {v_e}")
    print(f"M Dot (kg/s): {mdot}")
    print(f"Throat Area (m^2): {At}")
    print(f"Throat Diameter (in): {Dt_in}")
    print("----------------------------------")

    return(Dt_in)