N = 4

def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


def get_neighbors(state):
    neighbors = []

    for i in range(N):
        for j in range(i + 1, N):
            new_state = list(state)
            new_state[i], new_state[j] = new_state[j], new_state[i]

            neighbors.append((tuple(new_state), i, j))

    return neighbors


def print_board(state):
    for row in range(N):
        print(" ".join(["Q" if state[col] == row else "." for col in range(N)]))
    print()


def hill_climbing(initial_state):
    current = tuple(initial_state)

    while True:
        current_cost = cost(current)

        if current_cost == 0:
            print("Goal state reached!")
            return current

        print("\nCurrent state:", *current)
        print("Current cost:", current_cost)

        neighbors = get_neighbors(current)

        print("\nNeighbor states and costs:")

        for state, i, j in neighbors:
            print(
                f"Swap row {i} and row {j}: "
                f"{''.join(map(str, state))} "
                f"cost is {cost(state)}"
            )


        best_state, row1, row2 = min(
            neighbors,
            key=lambda item: cost(item[0])
        )

        best_cost = cost(best_state)

        if best_cost >= current_cost:
            print("\nLocal minimum reached.")
            print("No better neighbor exists.")
            return current

        print(f"\nSelected swap: row {row1} and row {row2}")
        current = best_state


initial_state = (3, 1, 2, 0)

solution = hill_climbing(initial_state)

print("\nFinal solution:", *solution)
print("Final cost:", cost(solution))
print("\nFinal Board:")
print_board(solution)