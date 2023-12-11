from solar_system import DynamicalSystem as ds
import matplotlib.pyplot as plt
import numpy as np
from solar_system import CelestialBody

solar = ds(400)

planets = (CelestialBody(
        solar,
        mass = 10_000 ,color ="yellow",
    ),
    CelestialBody(
        solar,
        position=np.array([150, 50, 0]),
        velocity=np.array([0, 5, 5]),color ="red"
    ),
    CelestialBody(
        solar,
        mass=20,
        position=np.array([100, -50, 150]),
        velocity=np.array([5, 0, 0]), color ="blue"
    )
)

while True:
    solar.dynamical_interaction()
    solar.update_all()
    solar.display_all()