from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "<h2>Hello World</h2>"