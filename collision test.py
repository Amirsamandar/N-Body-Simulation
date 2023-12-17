from solar_system import DynamicalSystem, CelestialBody
import numpy as np

solar = DynamicalSystem(400, projection2D =True ,restitution =0, closed = True)

Sun = CelestialBody(solar, mass = 10_000, color = "yellow")

CelestialBody(solar, position=np.array([150, 0., 0]), velocity=np.array([0, 0., 0]), color = "blue")



for _ in range(200):
    solar.dynamical_interaction()
    solar.update_all()
    solar.display_all()



