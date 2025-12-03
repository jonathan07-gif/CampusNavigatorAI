# Campus Navigator AI — Project Report

**Author:** Saroj Parajuli  
**Course:** Fundamentals in AI and ML  
**Project:** Campus Navigation Assistant — Search-Based Problem Solving Agent

---

## 1. Project Objective
Design an AI problem-solving agent to find routes between campus locations using classical AI search algorithms (BFS, DFS, A*). No machine learning is used.

## 2. Problem Statement
Given a campus map (graph), design an agent that accepts a start node and goal node and returns valid paths found by:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search (informed using heuristic)

## 3. Scope & Requirements

### Functional Requirements
1. Input: start and goal location names.
2. Output: paths found by BFS, DFS, and A*.
3. CLI: interactive and command-line modes.
4. Unit tests ensuring basic correctness.

### Non-Functional Requirements
- **Usability:** Simple CLI; easy to run.
- **Reliability:** Deterministic behavior for same input.
- **Maintainability:** Graph data stored in `data/nodes.csv` and graph module `core/graph.py`.
- **Explainability:** Show which algorithm produced each path.

## 4. System Architecture & Modules
- `app.py` — Main interface (interactive CLI).
- `core/graph.py` — Knowledge representation (graph).
- `core/search.py` — BFS, DFS, A* algorithm implementations.
- `core/heuristic.py` — Heuristic function for A*.
- `core/agent.py` — Agent class that orchestrates searches.
- `tests/` — Unit tests (`pytest`).

(See `docs/class_diagram.png` for UML class diagram.)

## 5. Design Decisions
- Graph represented as adjacency list (dictionary): simple and clear.
- BFS used for shortest path in unweighted graphs.
- DFS included for demonstration of uninformed search behavior.
- A* uses a simple heuristic (straight-line approximation values) to illustrate informed search.
- No learning or data-driven components — strictly symbolic AI.

## 6. Algorithms (brief)
- **BFS:** Explore level by level using a queue. Guaranteed shortest path in unweighted graphs.
- **DFS:** Explore deep paths first using a stack. May not return shortest path.
- **A\***: Use f(n)=g(n)+h(n). g(n) approximated by path length; h(n) provided by `heuristic()`.

## 7. Testing
- Unit tests in `tests/test_search.py` verify BFS returns a path from a start to goal.
- Run tests: `pytest -q`.

## 8. How to Run
1. Create venv: `python3 -m venv venv`  
2. Activate venv: `source venv/bin/activate` (mac/linux)  
3. Install (only pytest required): `pip install -r requirements.txt`  
4. Run: `python app.py` or `python -m core.cli --start Hostel --goal Library`

## 9. Extensions (future work)
- Read graph from CSV at runtime.
- Add weighted edges and show Dijkstra.
- Add GUI/Map visualization (Streamlit or Tkinter).
- Add multi-criteria heuristics (time, distance).

## 10. Conclusion
This project demonstrates core AI course concepts — knowledge representation, problem solving, uninformed/informed search — in a complete, explainable project suitable for coursework and demonstrations.

---