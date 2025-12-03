from collections import deque
import heapq

# -------- BFS (Uninformed Search) --------
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(path + [neighbor])

    return None


# -------- DFS (Uninformed Search) --------
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(path + [neighbor])

    return None


# -------- A* (Informed Search) --------
def astar(graph, start, goal, heuristic):
    pq = []
    heapq.heappush(pq, (0, [start]))
    visited = set()

    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                g = len(path)
                h = heuristic(neighbor, goal)
                f = g + h
                heapq.heappush(pq, (f, path + [neighbor]))

    return None