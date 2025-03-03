from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Welcome message for the Fantasy Sports Assistant app.
    return "<h1>Welcome to the Fantasy Sports Assistant!</h1><p>Your journey to smarter fantasy decisions begins here.</p>"

if __name__ == '__main__':
    app.run(debug=True)