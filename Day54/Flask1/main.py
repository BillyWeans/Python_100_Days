from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World!'

@app.route("/goodbye")
def goodbye_world():
    return 'Peace Out!!'

# Indicate variables to the flask decorator with <>
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f'Hello {name}, you are {number} years old!'

if __name__ == '__main__':
    app.run(debug=True)
