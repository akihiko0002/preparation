from flask import Flask , render_template
app=Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World."

@app.route("/<name>")
def greet(name):
    return name + "さん、はろー！"

@app.route("/template")
def template():
    py_name="fukuda"
    return render_template("index.html",name= py_name)

@app.route("/sarada")
def sarada():
    return render_template("sarada.html")

@app.route("/new")
def new():
    return render_template("new.html")

if __name__=='__main__':
    app.run(debug=True)