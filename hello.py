from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', 'world')
    return f'<h1>Hello, {name}!</h1>\n<p>Welcome to the website.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
