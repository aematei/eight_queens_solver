# Eight Queens Solver

A visual algorithm explorer for the classic Eight Queens puzzle, developed for CS 4200 - Artificial Intelligence (Cal Poly Pomona, Spring 2025).

## About the Eight Queens Problem

The Eight Queens puzzle is a classic chess problem that asks: "How can eight queens be placed on a standard 8×8 chess board so that no queen attacks any other queen?" A queen can attack any piece in the same row, column, or diagonal.

This problem is a common example used to teach backtracking algorithms and constraint satisfaction problems in artificial intelligence.

## Algorithm Explanation

The solution uses a backtracking algorithm that works as follows:

1. Start with an empty chess board
2. Try placing a queen in the first row
3. Move to the next row and try to place another queen where it cannot be attacked
4. If no safe position is found in the current row, backtrack to the previous row and try a different position
5. Repeat until all eight queens are placed successfully or all possibilities are exhausted

The algorithm's time complexity is O(n!), but optimizations significantly reduce the actual search space.

## How to Use the Application

1. Clone this repository
2. Install the required dependencies: `pip install flask`
3. Run the Flask application: `python app.py`
4. Open your browser and navigate to `http://localhost:8000`
5. Use the controls to:

- Play: Start the algorithm visualization
- Pause: Temporarily stop the animation
- Restart: Reset the board
- Speed slider: Adjust the animation speed

## Screenshot

![Eight Queens Solver in action](screenshot.png)
*(Screenshot placeholder - replace with an actual screenshot of your application)*

## Implementation Details

- Backend: Python with Flask
- Frontend: HTML, CSS, and Vue.js (no build step required)
- Algorithm visualization with step-by-step animation
- Interactive controls for educational exploration

## License

MIT License

---

Developed by Alex Matei for CS 4200 - Artificial Intelligence, Cal Poly Pomona (Spring 2025)
