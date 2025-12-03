# **Project Report – Campus Navigator AI**
### **A Search-Based Problem Solving Agent**
### **Author: Saroj Parajuli (B.Tech CSE)**
### **VIT Bhopal University**

---

## **1. Title of the Project**
**Campus Navigator AI – A Search-Based Problem-Solving Agent using BFS, DFS, and A\***

---

## **2. Introduction**
Artificial Intelligence (AI) provides multiple approaches for solving complex real-world problems.  
One of the fundamental approaches in AI is **search**, where an agent explores a state space to find the best possible solution.

This project implements a **Campus Navigation System** using:
- **Uninformed Search** → *BFS & DFS*  
- **Informed Search** → *A\**  
- **Heuristic-based reasoning**  
- **Graph-based knowledge representation**

The system finds the shortest, most efficient path between two locations inside a campus.

---

## **3. Objectives**
The main objectives of this project are:

- To design a **Problem-Solving Agent** using AI techniques  
- To represent the campus map as a **graph** (state space)  
- To apply **BFS**, **DFS**, and **A\*** for pathfinding  
- To compare search strategies  
- To generate explainable and deterministic results  

---

## **4. Problem Statement**
Given a campus with multiple buildings and connecting paths, a student needs to navigate from a **Start Location** to a **Goal Location**.

The system must:
- Accept Start and Goal inputs  
- Run BFS, DFS, and A\* algorithms  
- Display valid paths for each search method  
- Use heuristics to improve search efficiency  

---

## **5. System Requirements**

### **Hardware Requirements**
- Laptop/PC (Windows/Mac/Linux)
- Minimum RAM: 4GB
- Python installed

### **Software Requirements**
- Python 3.8+  
- VS Code  
- Required libraries: `pytest`

---

## **6. Methodology**

### **6.1 Knowledge Representation**
The campus map is stored as an **adjacency list** in `graph.py`.

### **6.2 Search Algorithms**
- **BFS:** Level-order traversal, guarantees shortest path  
- **DFS:** Explores deeper first, not optimal  
- **A\* Search:** Uses cost function `f(n) = g(n) + h(n)` for efficient search  

### **6.3 Heuristic Function**
A static heuristic table is stored in `heuristic.py`.

### **6.4 Agent Design**
`NavigationAgent` integrates:
- BFS  
- DFS  
- A\*  
- Graph

---

## **7. System Architecture**
The main components are:

- **Input Module** — Reads start & goal  
- **Agent Module** — Executes all search algorithms  
- **Graph Module** — Stores campus structure  
- **Heuristic Module** — Stores heuristic values  
- **Output Module** — Displays paths  

---

## **8. Flowchart / Diagrams**
Diagrams included in `/docs/`:
1. Class Diagram  
2. Use Case Diagram  
3. Sequence Diagram  
4. Architecture Diagram  

---

## **9. Implementation**
### **Main File:** `app.py`  
Handles input and prints BFS, DFS, and A\* results.

### **Core Modules:**  
- `graph.py` → Campus graph  
- `search.py` → BFS, DFS, A\*  
- `heuristic.py` → Heuristic values  
- `agent.py` → Problem-solving agent  

---

## **10. Sample Output**
=== Campus Navigation AI System ===
Enter start location: Hostel
Enter goal location: Library

— RESULTS —
BFS Path: [‘Hostel’, ‘Canteen’, ‘Library’]
DFS Path: [‘Hostel’, ‘Block A’, ‘Block B’, ‘Block C’, ‘Library’]
A* Path: [‘Hostel’, ‘Canteen’, ‘Library’]

---

## **11. Testing**
Unit testing done using **pytest**:

- `test_search.py` verifies BFS returns correct path  
- Ensures no runtime errors  
- Confirms correct graph traversal  

---

## **12. Results**
- BFS provided shortest path  
- DFS explored deeper paths first  
- A\* produced fastest & optimal path using heuristics  
- All algorithms performed correctly on campus graph  

---

## **13. Conclusion**
This project successfully demonstrates the use of **AI Search Techniques** in solving real-world navigation problems.  
It highlights the importance of:
- Graph-based state representation  
- Uninformed vs informed search  
- Heuristic-based reasoning  

The system is simple, effective, and easily extendable.

---

## **14. Future Enhancements**
- Weighted edges for more realistic navigation  
- Live campus map visualization  
- GUI using Tkinter or Streamlit  
- Voice-based input for accessibility  

---

## **15. References**
- Artificial Intelligence: A Modern Approach – Stuart Russell, Peter Norvig  
- Class lecture notes  
- Python official documentation  

---