from re import split
from functions import *

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# CELLS 0, 1, AND 2 ARE USED FOR COMPUTATION AND SHOULD NOT BE MODIFIED
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


with open('code.asmbf', 'r') as file:
    code = file.read()

# Remove comments from code
code = '\n'.join([line.split('#')[0] for line in code.split('\n')])
# Remove empty lines
code = '\n'.join([line for line in code.split('\n') if line])

res = ""
for line in code.split('\n'):
    split_line = line.split()
    if split_line[0] == 'ld':  # Load cell
        res += set_cell(int(split_line[1]), int(split_line[2]))
    elif split_line[0] == 'inc':  # Increment cell (negative for decriment)
        res += inc_cell(int(split_line[1]), int(split_line[2]))
    elif split_line[0] == 'add':  # add a b c: add a and b, output in c
        res += bf_add(int(split_line[1]), int(split_line[2]), int(split_line[3]))
    elif split_line[0] == 'sub':  # sub a b c: subtract a and b, output in c
        res += bf_sub(int(split_line[1]), int(split_line[2]), int(split_line[3]))
    elif split_line[0] == 'mul':  # mul a b c: multiply a and b, output in c
        res += bf_mul(int(split_line[1]), int(split_line[2]), int(split_line[3]))
    elif split_line[0] == 'div':
        res += bf_div(int(split_line[1]), int(split_line[2]), int(split_line[3]))
    elif split_line[0] == 'qdiv':
        res += bf_quick_div(int(split_line[1]), int(split_line[2]), int(split_line[3])) # Only works if quotient is integer (no remainder)
    elif split_line[0] == 'out':  # Output character from cell
        res += bf_print_chr(int(split_line[1]))
    elif split_line[0] == 'in':  # Input character to cell
        res += bf_input_chr(int(split_line[1]), str(split_line[2]))
    elif split_line[0] == 'lin':  # Input string to array of cells (define starting cell)
        res += bf_input_str(int(split_line[1]), str(' '.join(split_line[2:])))
    elif split_line[0] == 'lo':  # Output range of cells
        res += bf_output_range(int(split_line[1]), int(split_line[2]))
    elif split_line[0] == 'sa':  # Set array of cells (startcell, endcell, pattern)
        #Repeats values until the endcell (eg. sa 5 10 1 2 will repeat 1 2 between cells 5 and 10)
        res += bf_set_array(int(split_line[1]), int(split_line[2]), [int(i) for i in split_line[3:]])
    elif split_line[0] == 'gt': # Greater than
        res += bf_comparison(int(split_line[1]), int(split_line[2]), int(split_line[3]))
    elif split_line[0] == 'eq':
        res += bf_equals(int(split_line[1]), int(split_line[2]), int(split_line[3]))
    elif split_line[0] == 'fl':
        res += bf_floor(int(split_line[1]))
    elif split_line[0] == 'as': # Arithmetic sequence
        res += bf_set_arith_seq(int(split_line[1]), int(split_line[2]), int(split_line[3]), int(split_line[4]))
    elif split_line[0] == 'ia':  # Same as set_array, just increments existing values instead of reseting them
        res += bf_inc_array(int(split_line[1]), int(split_line[2]), [int(i) for i in split_line[3:]])
    elif split_line[0] == 'ias': # Increment existing values with arithmetic sequence
        res += bf_inc_arith_seq(int(split_line[1]), int(split_line[2]), int(split_line[3]), int(split_line[4]))
    elif split_line[0] == 'sp':  # Set an array of cells based on a polynomial
        res += bf_set_polynomial(int(split_line[1]), int(split_line[2]), [int(i) for i in split_line[3:]])
    elif split_line[0] == 'ip':  # Inc an array of cells based on a polynomial
        res += bf_inc_polynomial(int(split_line[1]), int(split_line[2]), [int(i) for i in split_line[3:]])
    elif split_line[0] == 'cp':
        res += bf_copy_cell(int(split_line[1]), int(split_line[2]))
    elif split_line[0] == 'or':
        res += bf_or(int(split_line[1]), int(split_line[2]), int(split_line[3]))
    elif split_line[0] == 'and':
        res += bf_and(int(split_line[1]), int(split_line[2]), int(split_line[3]))
    elif split_line[0] == 'not': # Input has to be 0 or 1
        res += bf_not(int(split_line[1]), int(split_line[2]))


    
    else:
        print(f'Unknown command: {line}')

# Optimizing motion, things like removing redundant moves 
# (>>><>> becomes >>>>, ++--+++ becomes +++, etc)

while res.find("<>") != -1:
    res = res.replace("<>", "")
while res.find("><") != -1:
    res = res.replace("><", "")
while res.find("-+") != -1:
    res = res.replace("-+", "")
while res.find("+-") != -1:
        res = res.replace("+-", "")

print(res)
