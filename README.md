## Abstract
This thesis explores the use of a **SAT solver** to solve shape-fitting puzzles by encoding
them as _Boolean satisfiability problems_. Users define an arbitrary board size and a list
of shapes, which remain fixed throughout the solving process. Each valid placement of a
shape is represented as a unique propositional variable, and the puzzle’s constraints related
to the shapes’ positions are translated into a _conjunctive normal form (CNF)_ formula. This
formula is then solved using the MiniSat solver through the **PySAT** library. The imple
mentation identifies valid shape arrangements and determines whether a solution exists,
successfully handling puzzles of small to moderate complexity. This work demonstrates
the effectiveness of SAT-based techniques in solving spatial logic problems.
