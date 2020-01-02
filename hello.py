from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

''' Decorator 語法筆記
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

hello = app.route('/'):
            def wrap():
                'warp the function'
                hello()
            
            return warp
'''