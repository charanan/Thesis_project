def load_input(filename):
    local_vars = {}
    with open(filename, 'r') as f:
        code = f.read()
        exec(code, {}, local_vars)

    if validate_input(local_vars['W'], local_vars['H'], local_vars['shapes']):
        return local_vars['W'], local_vars['H'], local_vars['shapes']
    else:
        exit()

def validate_input(W, H, shapes):
    # Validate board W and H
    if not isinstance(W, int) or not isinstance(H, int) or W <= 0 or H <= 0:
        print("W and H must be positive integers.")
        return False
    
    # Validate shapes
    total_coords = sum(len(shape) for shape in shapes)
    if total_coords > W * H:
        print("Invalid total coordinates of the shapes")
        return False

    for shape_id, shape in enumerate(shapes):
        if not isinstance(shape, list):
            print("Each shape must be a list of coordinates.")
            return False
        for coord in shape:
            if not (isinstance(coord, tuple) and len(coord) == 2):
                print(f"Shape {shape_id} has invalid coordinate format: {coord}")
                return False
            x, y = coord
            if not (isinstance(x, int) and isinstance(y, int)) or x < 0 or y < 0:
                print(f"Coordinates (in shape {shape_id}) must be positive integers: {coord}")
                return False
            if x >= W or y >= H:
                print(f"Shape {shape_id} has invalid coordinate against the board size.")
                return False
            
    return True
