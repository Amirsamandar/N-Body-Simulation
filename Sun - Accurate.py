from solar_system import DynamicalSystem, CelestialBody
import numpy as np

solar = DynamicalSystem(400, projection2D =True)

Sun = CelestialBody(solar, mass = 100, color = "yellow")
planets = (
    CelestialBody(
        solar,
        position=np.array([150, 50., 0]),
        velocity=np.array([0, 0., 0]), color = "blue"
    ),
    CelestialBody(
        solar,
        mass=20,
        position=np.array([100., -50, 150.]),
        velocity=np.array([0, 0., 0])
    )
)
for _ in range(100):
    solar.dynamical_interaction()
    solar.update_all()
    print(Sun.position)



print(f"the final {Sun.position}")