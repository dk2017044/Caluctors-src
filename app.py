from flask import Flask, render_template, request, jsonify
from sympy import sympify

app = Flask(__name__)

# Routes for pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# API endpoint for calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')

        # Basic input validation
        if not expression or len(expression) > 100:
            return jsonify({'error': 'Invalid or too long expression'})

        # Allow only safe characters
        allowed_chars = '0123456789+-*/(). '
        if not all(c in allowed_chars for c in expression):
            return jsonify({'error': 'Invalid characters in expression'})

        # Secure evaluation using sympy
        result = sympify(expression).evalf()
        return jsonify({'result': float(result)})

    except Exception as e:
        return jsonify({'error': f'Calculation failed: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)