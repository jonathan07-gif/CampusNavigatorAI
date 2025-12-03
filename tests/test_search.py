from core.graph import campus_graph
from core.search import bfs

def test_bfs_route():
    path = bfs(campus_graph, "Hostel", "Library")
    assert path[0] == "Hostel"
    assert path[-1] == "Library"