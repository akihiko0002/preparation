from flask import Flask
app=Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World."

@app.route("/<name>")
def greet(name):
    return name + "さん、はろー！"

if __name__=='__main__':
    app.run(debug=True)