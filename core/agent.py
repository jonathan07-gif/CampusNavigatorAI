from core.graph import campus_graph
from core.search import bfs, dfs, astar
from core.heuristic import heuristic

class NavigationAgent:
    def __init__(self):
        self.graph = campus_graph

    def solve(self, start, goal):
        return {
            "BFS": bfs(self.graph, start, goal),
            "DFS": dfs(self.graph, start, goal),
            "A*": astar(self.graph, start, goal, heuristic)
        }