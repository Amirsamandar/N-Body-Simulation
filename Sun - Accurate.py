from solar_system import DynamicalSystem, CelestialBody
import numpy as np

solar = DynamicalSystem(400, projection2D =True)

Sun = CelestialBody(solar, mass = 100_000, color = "yellow")

CelestialBody(solar, mass = 100, position=np.array([150, 20., 0]), velocity=np.array([20, 0., 0]), color = "blue")
CelestialBody(solar,mass= 100, position=np.array([150, 10., 0]), velocity=np.array([0, 20., 0]), color = "blue")


for _ in range(200):
    solar.dynamical_interaction()
    solar.update_all()
    solar.display_all()



