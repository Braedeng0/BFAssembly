## BF ASSEMBLY 
### Overview
**Welcome to BF Assembly**, an assembly language that compiles down to [brainfuck](https://esolangs.org/wiki/Brainfuck). BF is a wonderful, fun, and useful language, but it is not necessarily easy to code in. Similarly, machine code is also very difficult to code in, so assembly languages were developed to help aid in the writing of code. **BF Assembly** takes assembly instructions and compiles them into BF using python. Because BF is already so limiting and the compiler can't directly manipulate BF memory, the outputted PF code will most likely be much longer and and quite inefficient compared to normal BF code, but it serves the exact same purpose. Happy coding!

**Some Basic Instructions (And Warnings)**:
- Assembly code is written in the code.asmbf file (note: asmbf is assembly brainfuck)
- Cells 0, 1, and 2 are reserved for computation while cells >=3 are free to use. There is nothing stopping the user from using these cells, but the vast majority of operations use them, causing everything to be messed up. 
- Cells may be overritten by other instructions such as lin or by adding, multiplying, comparing, and other operations.
- Operations that have a designated output cell (like addition, subtraction, etc.) will reset both input cells.

### Operations
Note: ":" in the last parameter for an operator signifies that more parameters after that may be taken such as multiple words in **lin**

- **ld [cell] [value]** - "Load"; Loads a value to the specified cell  
- **inc [cell] [value]** - "Increment"; Increment cell (negative for decriment)  
- **add [cell1] [cell2] [outputcell]** - "Add"; Adds cell1 and cell2 and stores in outputcell  
- **sub [cell1] [cell2] [outputcell]** - "Subtract"; Subtracts cell2 from cell1 and stores in outputcell  
- **mul [cell1] [cell2] [outputcell]** - "Multiply"; Multiplies cell1 and cell2 and stores in outputcell  
- **div [cell1] [cell2] [outputcell]** - "Divide"; Divides cell1 by cell2 and stores in outputcell  
- **out [cell]** - "Output"; Outputs a char from a cell  
- **in [cell] [char]** - "Input"; Inputs a char to a cell  
- **lin [startcell] [str:]** - "Long Input"; Inputs a string into an array of cells starting at startcell  
- **lo [startcell] [endcell]** - "Long Output"; Outputs charecters in a range of cells from startcell to endcell  
- **sa [startcell] [endcell] [value:]** - "Set Array"; Loads a list of values into a range of cells (values will repeat if the number of values is shorter than the range of cells) (eg. sa 2 10 2 3  4...)
- **ia [startcell] [endcell] [value:]** - "Increment Array"; Same as **sa**, but increments cells instead of setting them
- **cp [cell1] [cell2] [outputcell]** - "Compare"; Compares two values and stores the result in outputcell (1 if cell1 > cell2 else 0)  
- **eq [cell1] [cell2] [outputcell]** - "Equal"; If cell1 == cell2 outputcell is set to 1 else 0
- **fl [cell]** - "Floor"; Sets cell to 1 if cell is not 0 else 0
- **as [startcell] [endcell] [firstterm] [secondterm]** - "[Set] Arithmetic Sequence"; Creates an arithmetic sequence from the starting cell to the end cell based off of the first two terms of the arithmetic sequence
- **ias [startcell] [endcell] [firstterm] [secondterm]** - "Increment Arithmetic Sequence"; Same as **as**, but increments cells instead of setting them
- **sp [startcell] [endcell] [coefficients:]** - "Set Polynomial"; Sets an array of cells to the result of a polynomial function, coefficients are read in lowest degree to highest degree
- **ip [startcell] [endcell] [coefficients:]** - "Increment Polynomial"; Same as **sp**, but increments cells instead of setting them