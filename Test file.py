import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class DynamicalSystem:
    def __init__(self, size):
        self.size = size
        self.bodies = []

        self.fig, self.ax = plt.subplots(1, 1, subplot_kw={"projection": "3d"}, figsize=(self.size / 50, self.size / 50))
        self.fig.tight_layout()
        self.ax.view_init(30, 30)

    def add_body(self, body):
        self.bodies.append(body)

    def update_all(self, frame):
        for body in self.bodies:
            body.motion()
        self.dynamical_interaction()
        self.display_all()

    def display_all(self):
        self.ax.clear()
        for body in self.bodies:
            body.display()
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))

    def dynamical_interaction(self):
        positions = np.array([body.position for body in self.bodies])
        masses = np.array([body.mass for body in self.bodies])

        for i, body in enumerate(self.bodies):
            other_positions = np.delete(positions, i, axis=0)
            differences = other_positions - body.position
            distances = np.linalg.norm(differences, axis=1)
            gravitational_forces = (masses[i] * masses[:-1] / distances**2)[:, np.newaxis]

            acceleration_vectors = gravitational_forces * (differences.T / distances).T
            total_acceleration = np.sum(acceleration_vectors, axis=0)

            body.velocity += total_acceleration / body.mass

class NBodies:
    def __init__(self, dynamical_box, mass, position=np.array([0., 0., 0.]), velocity=np.array([0., 0., 0.])):
        self.dynamical_box = dynamical_box
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.dynamical_box.add_body(self)

        self.display_size = int(max(np.abs(np.log2(self.mass)), 10))
        self.color = "black"

    def motion(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    def display(self):
        self.dynamical_box.ax.plot(
            *self.position, marker="o", markersize=self.display_size, color=self.color
        )

if __name__ == "__main__":
    solar_system = DynamicalSystem(size=50)

    sun = NBodies(solar_system, mass=10000, position=[0, 0, 0], velocity=[0, 0, 0], color="yellow")
    earth = NBodies(solar_system, mass=1, position=[10, 0, 0], velocity=[0, 0, 1], color="blue")
    moon = NBodies(solar_system, mass=0.01, position=[10, 2, 0], velocity=[0, 0, 2], color="gray")

    for _ in range(100):
        solar_system.update_all(_)
        plt.pause(0.01)

    plt.show()
