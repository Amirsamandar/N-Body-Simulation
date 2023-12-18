from solar_system import DynamicalSystem, CelestialBody
import numpy as np


system = DynamicalSystem(500, projection2D =True , closed = False )

Stars = (
    CelestialBody(system, mass = 10_000., position=np.array([40., 40, 40]), velocity=np.array([6., 0, 6]) , color = "purple"),
    CelestialBody(system,  mass = 10_000.,  position=np.array([-40., -40, 40]), velocity=np.array([-6., 0, -6]) , color = "blue"),
)

planets = (
    CelestialBody(
        system,
        mass = 10,
        position=np.array([100., 100, 0]),
        velocity=np.array([0, 5.5, 5.5]),
    ),
    CelestialBody(
        system,
        mass = 20.,
        position=np.array([0., 0, 0]),
        velocity=np.array([-11, 11., 0]),
    ),
)

while True:
    system.dynamical_interaction()
    system.update_all()
    system.display_all()

   