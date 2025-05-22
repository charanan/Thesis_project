from pysat.formula import CNF
from pysat.solvers import MinisatGH

from itertools import combinations


def solve_puzzle(W, H, shapes, degrees):

    ### POSSIBLE PLACEMENTS ###
    cnf = CNF()
    curr_var = 1
    placement_to_var = {}

    for shape_id, shape in enumerate(shapes):
        # Compute boundaries of this shape
        x_max = max(x for x, _ in shape)
        y_max = max(y for _, y in shape)

        # Save all possible positions (relative to anchor) of this shape on the board
        for dy in range (H - y_max):
            for dx in range(W - x_max):
                placement_to_var[(shape_id, dx, dy)] = curr_var
                curr_var += 1


    ### USING EVERY SHAPE ONCE ###
    for shape_id in range(len(shapes)):
        # Retrieve all placement variables of this shape
        vars_for_shape = [var for (id, _, _), var in placement_to_var.items() if id == shape_id]
        # At least one placement
        cnf.append(vars_for_shape)
        # At most one placement
        for v1, v2 in combinations(vars_for_shape, 2):
            cnf.append([-v1, -v2])


    ### NO OVERLAPS ###
    cell_to_vars = {}

    # Check which variables use the same cell
    for (id, dx, dy), var in placement_to_var.items():
        # Retrive actual placement of this shape -> exact position (cell) of each unit of the shape
        for x, y in shapes[id]:
            xi, yi = x+dx, y+dy
            
            if (xi, yi) not in cell_to_vars:
                cell_to_vars[(xi, yi)] = []
            # Add the placement variable to this cell -> a part of the shape uses the cell
            cell_to_vars[(xi, yi)].append(var)

    # No two variables share the same cell
    for cell_vars in cell_to_vars.values():
        for v1, v2 in combinations(cell_vars, 2):
            cnf.append([-v1, -v2])


    ### SOLVE THE SAT PROBLEM ###
    cell_to_shape = {}

    with MinisatGH(bootstrap_with=cnf) as solver:
        if solver.solve():
            model = solver.get_model()
            for (id, dx, dy), var in placement_to_var.items():
                if var in model:
                    print(f"Place shape {id} rotated by {degrees[id]} degree at position ({dx}, {dy})")

                    for x, y in shapes[id]:
                        cell_to_shape[(x+dx, y+dy)] = id

    return cell_to_shape