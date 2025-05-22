import itertools

from puzzle import solve_puzzle


ROTATIONS = [0, 90, 180, 270]

def rotate_shape(shape, degree):
    if degree == 90:
        return [(y, -x) for (x, y) in shape]
    elif degree == 180:
        return [(-x, -y) for (x, y) in shape]
    elif degree == 270:
        return [(-y, x) for (x, y) in shape]
    return shape

def normalize_shape(shape, W, H):
    min_x = min(x for x, _ in shape)
    min_y = min(y for _, y in shape)
    normalized = [(x - min_x, y - min_y) for (x, y) in shape]

    # Check boundaries
    max_x = max(x for x, y in normalized)
    max_y = max(y for x, y in normalized)
    if max_x >= W or max_y >= H:
        return None
    return normalized

def get_rotated_shapes(W, H, original_shapes, degrees):
    rotated_shapes = []

    for shape, deg in zip(original_shapes, degrees):
        rotated = rotate_shape(shape, deg)
        normalized = normalize_shape(rotated, W, H)

        if normalized is None:
            rotated_shapes = []
            break
        rotated_shapes.append(normalized)

    return rotated_shapes

def try_rotations(W, H, original_shapes):
    solution = {}

    # Establish all degree combinations
    for degrees in itertools.product(ROTATIONS, repeat=len(original_shapes)):
        rotated_shapes = get_rotated_shapes(W, H, original_shapes, degrees)
        if not rotated_shapes:
            continue

        # Try solving
        solution = solve_puzzle(W, H, rotated_shapes, degrees)

        if solution:
            return solution
    
    return solution