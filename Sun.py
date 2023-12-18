from solar_system import DynamicalSystem, CelestialBody
import numpy as np

solar = DynamicalSystem(400, projection2D =True , frame_speed = 0.0000001)

Sun = CelestialBody(solar, mass = 10_000, color = "yellow")
planets = (
    CelestialBody(
        solar,
        position=np.array([150, 50., 0]),
        velocity=np.array([0, 5., 5]), color = "blue"
    ),
    CelestialBody(
        solar,
        mass=20,
        position=np.array([100., -50, 150.]),
        velocity=np.array([5, 0., 0])
    )
)
while True:
    solar.dynamical_interaction()
    solar.update_all()
    solar.display_all()

   