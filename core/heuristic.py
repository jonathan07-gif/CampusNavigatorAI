H_values = {
    ("Hostel", "Library"): 5,
    ("Canteen", "Library"): 3,
    ("Block A", "Library"): 4,
    ("Block B", "Library"): 2,
    ("Block C", "Library"): 1,
}

def heuristic(node, goal):
    return H_values.get((node, goal), 0)