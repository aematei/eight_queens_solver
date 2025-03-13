from flask import Flask, render_template, jsonify
import os

import eight_queens

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve')
def solve():
    solution = eight_queens.get_solution()
    if solution is None:
        return jsonify({"error": "No solution found"}), 404
    return jsonify(solution)

@app.route('/solve_steps')
def solve_steps():
    steps = eight_queens.get_solution_steps()
    return jsonify(steps)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)