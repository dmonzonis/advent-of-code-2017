from copy import deepcopy

import numpy as np


class ParticleSystem:
    """Represents a system of particles that move independently in the same space.

    Also saves info about the initial state of the system.
    """

    def __init__(self, particles):
        """Generate particle system from a list of particles."""
        self.system = particles
        # Save a copy of the initial state of the system for reset
        self._initial = deepcopy(self.system)
        self.time = 0

    def update(self, t):
        """Update the state of the system after after a time t has passed."""
        for particle in self.system:
            particle.update(t)

    def reset(self):
        """Reset the system to the initial state."""
        self.system = deepcopy(self._initial)


class Particle:
    """Represents a particle that moves with constant acceleration in 3D space."""

    def __init__(self, id, pos, vel, acc):
        """Initialize the particle's state using initial conditions."""
        self.id = id
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def update(self, t):
        """Update position and velocity after a time t has passed."""
        self.pos = self.pos + t * self.vel + self.acc * t * (t + 1) / 2
        self.vel = self.vel + self.acc * t

    def manhattan_dist(self):
        """Return the Manhattan distance of the particle to the origin."""
        return np.sum(np.abs(self.pos))

    def __str__(self):
        """Print the id of the particle when printing the praticle."""
        return str(self.id)


def parse_initial_conditions(states):
    """Return a list of initial conditions for position, velocity and acceleration."""
    vectors = []
    for state in states:
        state = state.split(', ')
        initial_conditions = []
        for cond in state:
            initial_conditions.append(
                [int(i) for i in cond[cond.index('<') + 1:cond.index('>')].split(',')]
            )
        vectors.append(initial_conditions)

    return vectors


def create_particle_system(initial_conditions):
    """Return a list of particles initialized using the initial conditions."""
    particles = []
    id = 0
    for cond in initial_conditions:
        pos, vel, acc = cond
        particles.append(Particle(id, np.array(pos), np.array(vel), np.array(acc)))
        id += 1

    return ParticleSystem(particles)


def find_closest_to_origin(system):
    """Find the closest particle to the origin using the Manhattan distance."""
    closest = None
    dist = float('inf')
    for particle in system.system:
        particle_dist = particle.manhattan_dist()
        if particle_dist < dist:
            closest = particle
            dist = particle_dist
    return closest


def main():
    with open("input") as f:
        initial_conditions = parse_initial_conditions(f.read().splitlines())

    particle_system = create_particle_system(initial_conditions)
    particle_system.update(1000000)
    print("Part 1:", find_closest_to_origin(particle_system))


if __name__ == "__main__":
    main()
