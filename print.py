def print_result_board(W, H, cell_to_shape):
    print(f"\nBoard {W} x {H}:")

    max_id = max(cell_to_shape.values(), default=0)
    digits = len(str(max_id))

    for y in range(H):
        for x in range(W):
            if (x, y) in cell_to_shape:
                id = cell_to_shape[(x, y)]
                print(f"{id:0{digits}d}", end=" ")
            else:
                print("+" * digits, end=" ")
        print()