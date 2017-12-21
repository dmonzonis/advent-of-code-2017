import numpy as np


class Particle:
    def __init__(self, id, pos, vel, acc):
        """Initialize the particle's state using initial conditions."""
        self.id = id
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def update(self, t):
        """Updates position and velocity after a time t has passed."""
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


def create_particles(initial_conditions):
    """Return a list of particles initialized using the initial conditions."""
    particles = []
    id = 0
    for cond in initial_conditions:
        pos, vel, acc = cond
        particles.append(Particle(id, np.array(pos), np.array(vel), np.array(acc)))
        id += 1

    return particles


def update_system(particles, t):
    """Update the particle system after a time t has passed."""
    for particle in particles:
        particle.update(t)


def find_closest_to_origin(particles):
    """Find the closest particle to the origin using the Manhattan distance."""
    closest = None
    dist = float('inf')
    for particle in particles:
        particle_dist = particle.manhattan_dist()
        if particle_dist < dist:
            closest = particle
            dist = particle_dist
    return closest


def main():
    with open("input") as f:
        initial_conditions = parse_initial_conditions(f.read().splitlines())

    particles = create_particles(initial_conditions)
    update_system(particles, 1000000)
    print("Part 1:", find_closest_to_origin(particles))


if __name__ == "__main__":
    main()
