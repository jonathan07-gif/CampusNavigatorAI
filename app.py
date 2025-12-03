from core.agent import NavigationAgent

def main():
    print("=== Campus Navigation AI System ===")

    agent = NavigationAgent()

    start = input("Enter start location: ")
    goal = input("Enter goal location: ")

    result = agent.solve(start, goal)

    print("\n--- RESULTS ---")
    print("BFS Path:", result["BFS"])
    print("DFS Path:", result["DFS"])
    print("A* Path:", result["A*"])

if __name__ == "__main__":
    main()