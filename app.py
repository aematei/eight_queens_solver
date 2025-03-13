from flask import Flask, render_template, jsonify
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

if __name__ == '__main__':
    # Enable debug mode for hot reloading during development
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=8000, debug=True)