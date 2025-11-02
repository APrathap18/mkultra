import numpy as np
import math as math
from rocketcea.cea_obj import CEA_Obj
import matplotlib.pyplot as plt
import pyfluids as Fluid
oxName = 'GOX'
fuelName = 'RP1'
pamb = 14.7 # psia
#C = 0.85
#Cd = 0.85
g = 1.26 #ox
P0 = 300*6894.76 #Pa
rhoRP1 = 810 #kg/m^3
rhoGOX = 1.429 #kg/m^3, 8.9497e-1
P1 = 300*6894.76 #Pa
P2 = 150*6894.76 #Pa, chamber pressure
mdot = 0.014279838482639268 #kg/s
qm = mdot

#GH2_pyfluids = Fluid(FluidsList.Hydrogen).with_state(Input.pressure(feed_press_f_pa), Input.temperature(20))
#GH2_rho = GH2_pyfluids.density # Hydrogen density at manifold pressure and ambient temperature (kg/m^3)

#RP-1, incompressible flow
#qdot = C * A*sqrt(2*dens*(P1-P2)) #incompressible, m^3/s
CA = qm/(math.sqrt(2*rhoRP1*(P1-P2)))
print(f"RP1 Orifice Area: {CA/10**-6} mm^2")  #output in mm^2

#GOX, compressible flow
#mdot = Cd*A * sqrt(g*dens*P0((2/g+1))^((g+1)/(g-1))) #compressible, kg/s
CdA = mdot/(math.sqrt(g*rhoGOX*P0*((2/g+1))**((g+1)/(g-1))))
#print(f"LOx Orifice Count: {num_LOx_orifices}")
print(f"GOX Orifice Area: {CdA/10**-6} mm^2")  #output in mm^2