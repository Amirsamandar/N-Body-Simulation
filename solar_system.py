import numpy as np
import matplotlib.pyplot as plt

class DynamicalSystem:
    
    def __init__(self, size):
        
        self.size = size
        self.bodies = []

        self.fig , self.ax = plt.subplots(1,1, subplot_kw={"projection" : "3d"}, figsize = (self.size/50 , self.size/50))
        self.fig.tight_layout()

    def add_body(self, body):
       self.bodies.append(body)

    
    def update_all(self):
        for body in self.bodies:
            body.motion()
            body.display()

    def display_all(self):
        self.ax.set_xlim((-self.size/2,self.size/2))
        self.ax.set_ylim((-self.size/2,self.size/2))
        self.ax.set_zlim((-self.size/2,self.size/2))
        plt.pause(0.001)
        self.ax.clear()
   



class NBodies:

    def __init__(self,dynamics, mass , position = np.array([0,0,0]), velocity=np.array([0,0,0])):

        self.dynamics = dynamics
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.dynamics.add_body(self)

        self.display_size = max( np.log2(self.mass) , 10 )

        self.color = "black"

    def motion(self):

        self.position = (
            self.position[0]+self.velocity[0],
            self.position[1]+self.velocity[1],
            self.position[2]+self.velocity[2])
        

    def display(self):
        self.dynamics.ax.plot(*self.position,marker="o", markersize=self.display_size , color = self.color)
      



   
        

   
   
       




   