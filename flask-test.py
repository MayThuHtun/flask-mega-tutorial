from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <html>
    <head><title> This my flask app MTT.</title></head>
    <body><h1>Hello from Flask.May Thu Htun</h1></body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
