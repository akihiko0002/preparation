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

if __name__=='__main__':
    app.run(debug=True)