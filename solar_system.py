import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

class DynamicalSystem:
    def __init__(self, size, projection2D = False , view = (0,0)):
        # Initialize the dynamical system with a specified size
        self.size = size
        self.projection2D = projection2D
        self.bodies = []
        self.view = view 

        # Create a 3D subplot for visualization
        if projection2D:
            self.fig =  plt.figure(figsize =(self.size / 25, self.size / 25))
            self.ax3D = self.fig.add_subplot(1, 2, 1, projection = '3d')
            self.ax2D = self.fig.add_subplot(1,2,2)
            self.fig.tight_layout()
            self.ax3D.view_init(10, 0)
        else:
            self.fig, self.ax =  plt.subplots(1, 1, subplot_kw={"projection": "3d"}, figsize=(self.size / 50, self.size / 50))
            self.fig.tight_layout()
            self.ax.view_init(self.view[0], self.view[1])

    def add_body(self, body):
        # Add a celestial body to the system
        self.bodies.append(body)

    def update_all(self):
        # Update the motion and display of all celestial bodies in the system
        self.bodies.sort(key= lambda item: item.position[0])
        for body in self.bodies:
            body.motion()
            body.display()

    def display_all(self): 
        # Display all celestial bodies in the system
        if self.projection2D:
           plt.pause(0.01)
           self.ax3D.clear()
           self.ax3D.set_xlim((-self.size / 2, self.size / 2))
           self.ax3D.set_ylim((-self.size / 2, self.size / 2))
           self.ax3D.set_zlim((-self.size / 2, self.size / 2))
           self.ax2D.set_xlim((-self.size / 2, self.size / 2))
           self.ax2D.set_ylim((-self.size / 2, self.size / 2))
        else:
           plt.pause(0.01)
           self.ax.clear()
           self.ax.set_xlim((-self.size / 2, self.size / 2))
           self.ax.set_ylim((-self.size / 2, self.size / 2))
           self.ax.set_zlim((-self.size / 2, self.size / 2))


    def dynamical_interaction(self):
        # Calculate gravitational interactions between all pairs of celestial bodies
        bodies_copy = self.bodies.copy()
        # Generate pairs of bodies
        body_pairs = combinations(bodies_copy, 2)
        # Apply gravitational interaction for each pair
        for first, second in body_pairs:
            first.gravitational_interaction(second)
        # bodies_copy = self.bodies.copy()
        # for idx, first in enumerate(bodies_copy):
        #     for second in bodies_copy[idx + 1:]:
        #         first.gravitational_interaction(second)




class NBodies:
    def __init__(self, dynamical_box, mass, position=np.array([0., 0., 0.]), velocity=np.array([0., 0., 0.])):
        # Initialize a celestial body with mass, position, and velocity
        self.dynamical_box = dynamical_box
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.dynamical_box.add_body(self)

        # Determine the display size based on the mass
        self.display_size = int(max(2*np.log2(self.mass), 10))
        self.color = "black"

    def motion(self):
        # Update the position of the celestial body based on its velocity
        self.position += self.velocity

    def display(self):
        # Display the celestial body in the 3D plot
        if self.dynamical_box.projection2D :
            self.dynamical_box.ax3D.plot(*self.position, marker="o", markersize=self.display_size + self.position[0] / 30, color=self.color)
            self.dynamical_box.ax3D.plot(self.position[0],self.position[1], -self.dynamical_box.size/2 , marker="o", markersize=self.display_size/2 , color = "grey")
            self.dynamical_box.ax2D.plot(self.position[0],self.position[1],  marker="_",color=self.color)
        else:
           self.dynamical_box.ax.plot(*self.position, marker="o", markersize=self.display_size + self.position[0] / 30, color=self.color)
        
    def gravitational_interaction(self, other):
        # Calculate gravitational interaction between two celestial bodies
        G = 1
        distance_vec = self.position - other.position
        distance_mag = np.sqrt(distance_vec @ distance_vec)
        gravity_force = G * self.mass * other.mass / distance_mag**2
        self.velocity += -(gravity_force / (distance_mag * self.mass)) * distance_vec
        other.velocity += (gravity_force / (distance_mag * other.mass)) * distance_vec




class CelestialBody(NBodies): 
    def __init__(self, dynamical_box, mass=10., position=np.array([0.0, 0.0, 0.0]), velocity=np.array([0.0, 0.0, 0.0]), color="black"):
        # Initialize a celestial body with additional properties such as color
        super(CelestialBody, self).__init__(dynamical_box, mass, position, velocity)
        self.color = color


