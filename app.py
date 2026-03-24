from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Flask CI/CD Demo!',
        'status': 'success'
    })


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'flask-action'
    })


@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({
        'greeting': f'Hello, {name}!',
        'status': 'success'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
