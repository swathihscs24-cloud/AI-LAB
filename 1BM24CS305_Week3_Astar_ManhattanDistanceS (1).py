
import heapq

START = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Heuristic: sum of Manhattan distances
def heuristic(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile == 0:
            continue

        goal_index = GOAL.index(tile)

        current_row, current_col = divmod(i, 3)
        goal_row, goal_col = divmod(goal_index, 3)

        distance += (
            abs(current_row - goal_row)
            + abs(current_col - goal_col)
        )

    return distance


def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_blank = nr * 3 + nc
            new_state = list(state)

            new_state[blank], new_state[new_blank] = (
                new_state[new_blank], new_state[blank]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def display(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])


def a_star(start, goal):
    queue = [(heuristic(start), 0, start)]

    parent = {start: None}
    cost_so_far = {start: 0}
    expanded = 0

    while queue:
        f, g, current = heapq.heappop(queue)

        if g != cost_so_far[current]:
            continue

        expanded += 1

        if current == goal:
            path = []
            state = current

            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()

            print("\nSolution found!")
            print("Total moves:", len(path) - 1)
            print("Expanded nodes:", expanded)

            for step, state in enumerate(path):
                h = heuristic(state)
                print(f"\nStep {step}: g={step}, h={h}, f={step + h}")
                display(state)

            return

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if (neighbor not in cost_so_far or
                    new_g < cost_so_far[neighbor]):

                cost_so_far[neighbor] = new_g
                parent[neighbor] = current
                h = heuristic(neighbor)

                heapq.heappush(
                    queue, (new_g + h, new_g, neighbor)
                )

    print("No solution found.")


a_star(START, GOAL)
