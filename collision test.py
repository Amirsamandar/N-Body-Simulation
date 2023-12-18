from solar_system import DynamicalSystem, CelestialBody
import numpy as np

solar = DynamicalSystem(400, time_step =0.5, projection2D =True ,restitution =1, closed = True)

Sun = CelestialBody(solar, mass = 10_000, color = "yellow")

CelestialBody(solar, position=np.array([0.0,150., 0]), velocity=np.array([0, 0., 0]), color = "blue")



for _ in range(200):
    solar.dynamical_interaction()
    solar.update_all()
    solar.display_all()



