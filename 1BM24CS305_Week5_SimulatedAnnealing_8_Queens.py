import random
import math

N = 8

def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


def random_neighbor(state):
    neighbor = list(state)

    i, j = random.sample(range(N), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

    return tuple(neighbor), i, j


def print_board(state):
    for row in range(N):
        print(" ".join(["Q" if state[col] == row else "." for col in range(N)]))
    print()


def simulated_annealing(initial_state):
    current = tuple(initial_state)
    T = 10.0
    cooling_rate = 0.95
    min_temperature = 0.01
    count = 0

    while T > min_temperature:
        count = count + 1
        current_cost = cost(current)
        print("\nIteration", count)

        print("\nCurrent state:", *current)
        print("Current cost:", current_cost)
        print("Temperature:", round(T, 3))

        if current_cost == 0:
            print("Goal state reached!")
            return current

        next_state, i, j = random_neighbor(current)
        next_cost = cost(next_state)

        delta_E = current_cost - next_cost

        print(f"Swap row {i} and row {j}:",
              *next_state)
        print("Neighbor cost:", next_cost)
        print("Delta E:", delta_E)

        if delta_E > 0:
            current = next_state
            print("Better state accepted.")

        else:
            probability = math.exp(delta_E / T)
            r = random.random()

            print("Acceptance probability:",
                  round(probability, 4))
            print("Random number:", round(r, 4))

            if r < probability:
                current = next_state
                print("Neighbor accepted.")
            else:
                print("Neighbor rejected.")

        T *= cooling_rate

    print("\nTemperature reached minimum.")
    print("Final state:", *current)
    print("Final cost:", cost(current))

    return current


initial_state = (0, 1, 2, 3, 4, 5, 6, 7)
solution = simulated_annealing(initial_state)

print("\nReturned state:", *solution)
print("Returned cost:", cost(solution))
print("\nFinal Board:")
print_board(solution)