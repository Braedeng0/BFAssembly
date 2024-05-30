from numpy.polynomial import Polynomial

current_cell = 0  # Keep track of the current cell

def move_to_cell(cell: int) -> str:
    global current_cell
    res = ""
    if cell > current_cell:
        res += ">" * (cell - current_cell)
    elif cell < current_cell:
        res += "<" * (current_cell - cell)
    current_cell = cell
    return res


def set_cell(cell: int, value: int) -> str:
    global current_cell
    res = ""
    res += move_to_cell(cell)
    res += "[-]"  # Clear cell
    if value >= 3*cell:  # Only use computation cells if it is worth it (in general)
        res += move_to_cell(0)  # Move to cell 0 (computation cell)
        div, mod = divmod(value, 10)
        res += "+" * div + "[>++++++++++<-]>"  # 10 * div
        res += "+" * mod  # mod
        current_cell += 1
        res += "[-" + move_to_cell(cell) + "+" + move_to_cell(
            1) + "]"  # Move back to cell and add value to it
        res += move_to_cell(cell)  # Move back to the cell
    else:
        res += "+" * value  # Add value to cell
    return res

def inc_cell(cell: int, value: int) -> str:
    global current_cell
    res = ""
    res += move_to_cell(cell)
    if value >= 3*cell:  # Only use computation cells if it is worth it (in general)
        res += move_to_cell(0)  # Move to cell 0 (computation cell)
        div, mod = divmod(value, 10)
        res += "+" * div + "[>++++++++++<-]>"  # 10 * div
        res += "+" * mod  # mod
        current_cell += 1
        res += "[-" + move_to_cell(cell) + "+" + move_to_cell(
            1) + "]"  # Move back to cell and add value to it
        res += move_to_cell(cell)  # Move back to the cell
    else:
        res += "+" * value  # Add value to cell
    return res


def bf_add(cell1: int, cell2: int, outputCell=0) -> str:
    global current_cell
    res = ""

    res += move_to_cell(cell1)  # Move to cell1
    res += "[-" + move_to_cell(outputCell) + "+" + move_to_cell(
        cell1) + "]"  # Move to outputCell and add cell1 to it
    res += move_to_cell(cell2)  # Move to cell2
    res += "[-" + move_to_cell(outputCell) + "+" + move_to_cell(
        cell2) + "]"  # Move to outputCell and add cell2 to it
    res += move_to_cell(outputCell)  # Move back to the output cell

    return res


def bf_sub(cell1: int, cell2: int, outputCell=0) -> str:
    global current_cell
    res = ""

    res += move_to_cell(cell1)  # Move to cell1
    res += "[-" + move_to_cell(outputCell) + "+" + move_to_cell(
        cell1) + "]"  # Move to outputCell and add cell1 to it
    res += move_to_cell(cell2)  # Move to cell2
    res += "[-" + move_to_cell(outputCell) + "-" + move_to_cell(
        cell2) + "]"  # Move to outputCell and subtract cell2 from it
    res += move_to_cell(outputCell)  # Move back to the output cell

    return res


def bf_mul(cell1: int, cell2: int, outputCell: int) -> str:
    global current_cell
    res = ""
    # Adds cell1 to outputCell cell2 times
    res += move_to_cell(outputCell)  # Move to output cell
    res += "[-]"  # Clear cell
    res += move_to_cell(cell1)  # Move to cell1
    res += "[-" + move_to_cell(0) + "+" + move_to_cell(
        cell1) + "]"  # Move to cell1 to cell 0
    res += move_to_cell(cell2)  # Move to cell2
    res += "["  # Start loop
    res += move_to_cell(0)  # Move to cell 0
    res += "[-" + move_to_cell(outputCell) + "+" + move_to_cell(
        1) + "+" + move_to_cell(0) + "]"  # Add cell0 to outputCell and cell1
    res += move_to_cell(1) + "[-<+>]"  # Move cell1 back to cell0
    res += move_to_cell(cell2) + "-"  # Subtract 1 from cell2
    res += "]"  # End loop
    res += move_to_cell(0)  # Move to cell 0
    res += "[-]"  # Clear cell 0
    res += move_to_cell(outputCell)  # Move back to output cell
    return res

def bf_div(cell1: int, cell2: int, outputCell: int) -> str:
    global current_cell
    return "TODO"###################################### TODO #############################################

def bf_print_chr(cell: int) -> str:
    global current_cell
    res = ""
    res += move_to_cell(cell)
    res += "."
    return res

def bf_input_chr(cell: int, char: str) -> str:
    global current_cell
    newVal = ord(char)
    res = ""
    res += set_cell(cell, newVal)
    return res

def bf_input_str(startCell: int, string: str) -> str:
    global current_cell
    res = ""
    for cellOffeset, char in enumerate(string):
        res += bf_input_chr(startCell + cellOffeset, char)
    return res

def bf_output_range(startCell: int, endCell: int) -> str:
    global current_cell
    res = ""
    for cell in range(startCell, endCell + 1):
        res += bf_print_chr(cell)
    return res

def bf_set_array(startCell: int, endCell: int, value: list[int]) -> str:
    global current_cell
    res = ""
    for i, cell in enumerate(range(startCell, endCell + 1)):
        res += set_cell(cell, value[i % len(value)])
    return res

def bf_comparison(cell1: int, cell2: int, outputCell: int) -> str:
    # Returns 1 if cell1 > cell2, 0 otherwise in outputCell
    global current_cell
    res = ""
    # Clear output cell
    res += move_to_cell(outputCell)
    res += "[-]"
    res += move_to_cell(cell1)
    res += "[" + move_to_cell(0) + "+"
    res += move_to_cell(cell2) + "[-" + move_to_cell(0) + "[-]" + move_to_cell(1) + "+" + move_to_cell(cell2) + "]"
    res += move_to_cell(0) + "[-" + move_to_cell(outputCell) + "+" + move_to_cell(0) + "]"
    res += move_to_cell(1) + "[-" + move_to_cell(cell2) + "+" + move_to_cell(1) + "]"
    res += move_to_cell(cell2) + "-" + move_to_cell(cell1) + "-" + "]"
    # Clear cell1 and cell2
    res += move_to_cell(cell1) + "[-]"
    res += move_to_cell(cell2) + "[-]"
    return res

def bf_equals(cell1: int, cell2: int, outputCell: int) -> str:
    global current_cell
    res = ""
    res += move_to_cell(cell1)
    res += "[-" + move_to_cell(cell2) + "-" + move_to_cell(cell1) + "]"
    res += "+" + move_to_cell(cell2)
    res += "[" + move_to_cell(cell1) + "-" + move_to_cell(cell2) + "[-]" + "]"
    # Move result to output cell
    res += move_to_cell(cell1) + "[-" + move_to_cell(outputCell) + "+" + move_to_cell(cell1) + "]"
    return res

def bf_floor(cell: int) -> str:
    global current_cell
    res = ""
    res += move_to_cell(cell)
    # If cell is not 0, clear it and add 1
    res += "[[-]" + move_to_cell(0) + "+" + move_to_cell(cell) + "]"
    # Result is in cell 0, move it to cell
    res += move_to_cell(0)
    res += "[-" + move_to_cell(cell) + "+" + move_to_cell(0) + "]"
    return res

def bf_set_arith_seq(startCell: int, endCell: int, val1: int, val2: int) -> str:
    global current_cell
    m = val2 - val1
    res = ""
    for i, cell in enumerate(range(startCell, endCell + 1)):
        res += set_cell(cell, val1 + m * i)
    return res

def bf_inc_array(startCell: int, endCell: int, value: list[int]) -> str:
    global current_cell
    res = ""
    for i, cell in enumerate(range(startCell, endCell + 1)):
        res += inc_cell(cell, value[i % len(value)])
    return res

def bf_inc_arith_seq(startCell: int, endCell: int, val1: int, val2: int) -> str:
    global current_cell
    m = val2 - val1
    res = ""
    for i, cell in enumerate(range(startCell, endCell + 1)):
        res += inc_cell(cell, val1 + m * i)
    return res

def bf_set_polynomial(startCell: int, endCell: int, coefs: list[int]) -> str:
    global current_cell
    poly = Polynomial(coefs)
    res = ""
    for i, cell in enumerate(range(startCell, endCell + 1)):
        res += set_cell(cell, int(poly(i)))
    return res

def bf_inc_polynomial(startCell: int, endCell: int, coefs: list[int]) -> str:
    global current_cell
    poly = Polynomial(coefs)
    res = ""
    for i, cell in enumerate(range(startCell, endCell + 1)):
        res += inc_cell(cell, int(poly(i)))
    return res