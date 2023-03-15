from flask import Flask
app = flask(__name__)

@app.route('/')
def hello();
    """Return a friendly HTTP greeting."""
    print("I am inside help world")
    return 'Hello World!'
