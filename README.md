# N-Body Simulation

This Python script simulates the motion and interaction of celestial bodies in a dynamical system. It models gravitational forces and inelastic collisions between celestial bodies.

## Overview

The simulation consists of three classes:

1. **DynamicalSystem:**
   - Represents the overall dynamical system containing celestial bodies.
   - Allows for the addition of celestial bodies, updates their motion, and displays their positions.
   - Calculates gravitational interactions between celestial bodies.

2. **NBodies:**
   - Represents a celestial body in the system.
   - Defines parameters such as mass, position, velocity, and density.
   - Updates the body's motion, displays it in the 3D plot, and calculates gravitational interactions with other bodies.

3. **CelestialBody(NBodies):**
   - Inherits from NBodies and adds properties like color to represent a celestial body with additional visual features.

## Usage

```python
# Example usage:
time_step = 0.01  # Choose an appropriate time step
solar = DynamicalSystem(400, time_step, projection2D=True, restitution=0, closed=True)
body1 = CelestialBody(solar, mass=10., position=np.array([0., 20., 0.]), velocity=np.array([1., 0., 0.]), density=2,
                      color="red")
body2 = CelestialBody(solar, mass=15., position=np.array([0., -20., 0.]), velocity=np.array([-1., 0., 0.]), density=2,
                      color="blue")
solar.dynamical_interaction()
solar.update_all()
solar.display_all()
plt.show()
```

Note: Ensure that the required libraries (`numpy` and `matplotlib`) are installed before running the code.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Amirsamandar/n-body-simulation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd n-body-simulation
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the simulation:

   ```bash
   python solar_system.py
   ```

## Dependencies

- `numpy`: For numerical operations.
- `matplotlib`: For 3D plotting.

## Contributing

Contributions are welcome! If you find any issues or have improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to replace placeholders like `your-username` in the clone URL with your actual GitHub username. Additionally, you might want to include a `requirements.txt` file with the dependencies mentioned in the "Dependencies" section.
