import numpy as np
import matplotlib.pyplot as plt

class DynamicalSystem:
    def __init__(self, size):
        self.size = size
        self.bodies = []

        self.fig, self.ax = plt.subplots(1, 1, subplot_kw={"projection": "3d"}, figsize=(self.size / 50, self.size / 50))
        self.fig.tight_layout()
        self.ax.view_init(0, 0)

    def add_body(self, body):
        self.bodies.append(body)

    def update_all(self):
        for body in self.bodies:
            body.motion()
            body.display()

    def display_all(self): 
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        plt.pause(0.01)
        self.ax.clear()

    def dynamical_interaction(self):
        for index, body in enumerate(self.bodies):
            for other in self.bodies[index + 1:]:
                body.gravitational_interaction(other)


class NBodies:
    def __init__(self, dynamical_box, mass, position=np.array([0., 0., 0.]), velocity=np.array([0., 0., 0.])):
        self.dynamical_box = dynamical_box
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.dynamical_box.add_body(self)

        self.display_size = int(max(np.log2(self.mass), 10))
        self.color = "black"

    def motion(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    def display(self):
        self.dynamical_box.ax.plot(*self.position, marker="o", markersize=self.display_size, color=self.color)
        
     

    def gravitational_interaction(self, other):
        G = 1.
        distance_vec = np.array(self.position - other.position)
        distance_mag = np.sqrt(np.sum(distance_vec ** 2))
        gravity_force = G * self.mass * other.mass / distance_mag** 2
        self.velocity[0] += (gravity_force / (distance_mag * self.mass)) * distance_vec[0]
        self.velocity[1] += (gravity_force / (distance_mag * self.mass)) * distance_vec[1]
        self.velocity[2] += (gravity_force / (distance_mag * self.mass)) * distance_vec[2]
        other.velocity[0] += -(gravity_force / (distance_mag * other.mass)) * distance_vec[0]
        other.velocity[1] += -(gravity_force / (distance_mag * other.mass)) * distance_vec[1]
        other.velocity[2] += -(gravity_force / (distance_mag * other.mass)) * distance_vec[2]







class CelestialBody(NBodies): 
    def __init__(self, dynamical_box, mass=10, position=np.array([0.0, 0.0, 0.0]), velocity=np.array([0.0, 0.0, 0.0]), color="black"):
        super(CelestialBody, self).__init__(dynamical_box, mass, position, velocity)
        self.color = color






