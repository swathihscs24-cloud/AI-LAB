
from collections import deque

def print_grid(s):
    for i in range(0, 9, 3):
        print(*s[i:i+3])
    print()

def dfs(start, goal):
    q = deque([(start, [])])
    visited = {start}

    while q:
        state, path = q.popleft()

        if state == goal:

          for s in path + [state]:

            print_grid(s)
          print("goal reached")
          return

        zero = state.index(0)

        for m in [-3, 3, -1, 1]:
            p = zero + m
            if 0 <= p < 9:
                if m in (-1, 1) and zero // 3 != p // 3:
                    continue

                new = list(state)
                new[zero], new[p] = new[p], new[zero]
                new = tuple(new)

                if new not in visited:
                    visited.add(new)
                    q.append((new, path + [state]))

start = (1, 2, 3, 0, 4, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

dfs(start, goal)


    success = iterative_deepening_search(start_state, goal_state)
    if not success:
        print("Goal not found within the depth limit of 30.")
