# Campus graph representation (Knowledge Representation)

campus_graph = {
    "Hostel": ["Canteen", "Block A"],
    "Canteen": ["Hostel", "Library", "Block B"],
    "Library": ["Canteen", "Block C"],
    "Block A": ["Hostel", "Block B"],
    "Block B": ["Block A", "Canteen", "Block C"],
    "Block C": ["Block B", "Library"]
}