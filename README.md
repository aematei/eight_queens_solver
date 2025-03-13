# Eight Queens Algorithm

The Eight Queens algorithm is a classic problem in computer science and combinatorial optimization. The goal is to place eight queens on an 8x8 chessboard such that no two queens threaten each other. This means that no two queens can be in the same row, column, or diagonal.

## Algorithm Explanation

1. **Initialize the Board**: Create an 8x8 board initialized with zeros. Each cell represents a position on the chessboard, and a value of 1 indicates a queen is placed there.

2. **Check Safety**: For each position on the board, check if placing a queen there is safe. A position is considered safe if no other queens threaten it. This involves checking:
   - The column of the position.
   - The upper left diagonal of the position.
   - The upper right diagonal of the position.

3. **Place Queens Recursively**: Use a recursive function to place queens on the board. Start from the first row and attempt to place a queen in each column. If placing a queen in a column is safe, place the queen and move to the next row. If placing a queen in any column of the current row is not possible, backtrack to the previous row and move the queen to the next column.

4. **Print the Solution**: Once all queens are placed on the board such that no two queens threaten each other, print the board.

## Steps

1. **Initialize the Board**:
   ```python
   n = 8
   board = [[0] * n for _ in range(n)]