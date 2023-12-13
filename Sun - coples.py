from solar_system import DynamicalSystem, CelestialBody
import numpy as np

system = DynamicalSystem(size=400, projection2D=True , view = (10,0))

# Sun
sun = CelestialBody(system, mass=1000, position=np.array([0.0, 0.0, 0.0]), velocity=np.array([0.0, 0.0, 0.0]), color="yellow")

# Planets
mercury = CelestialBody(system, mass=1, position=np.array([30.0, 0.0, 0.0]), velocity=np.array([0.0, 1.3, 0.0]), color="grey")
venus = CelestialBody(system, mass=3, position=np.array([50.0, 0.0, 0.0]), velocity=np.array([0.0, 2.5, 0.0]), color="orange")
earth = CelestialBody(system, mass=5, position=np.array([80.0, 0.0, 0.0]), velocity=np.array([0.0, 2.0, 0.0]), color="blue")
mars = CelestialBody(system, mass=2, position=np.array([110.0, 0.0, 0.0]), velocity=np.array([0.0, 1.5, 0.0]), color="red")

# Simulate the solar system for a number of steps
for _ in range(500):
    system.dynamical_interaction()
    system.update_all()
    system.display_all()