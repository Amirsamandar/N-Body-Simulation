from solar_system import DynamicalSystem as ds
import matplotlib.pyplot as plt
import numpy as np
from solar_system import NBodies

solar = ds(400)
body = NBodies(solar,100,velocity=np.array([1,1,1]))

for _ in range(100):
    solar.update_all()
    solar.display_all()