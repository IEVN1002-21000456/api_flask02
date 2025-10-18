from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Mundo!"

@app.route('/hola')
def about():
    return "Hola"

@app.route('/user/<string:user>')
def user(user):
    return "Hello,{user}!"

@app.route('/numero/<int:num>')
def user(num):
    return "el numero es,{num}!"

@app.route('/suma/<int:num1>/<int:num2>')
def user(num1, num2):
    return "el numero es: {num1 + num2}!"

@app.route('/user/<int:id>/<string:username>')
def user(id,username):
    return "ID: {} nombre:{}".format(id.username)

@app.route('/suma/<float:n1>/<float:n2')
def user(n1,n2):
    return "la suma es:{}".format(n1+n2)

@app.route("/default/")
@app.route("/default/<string:dft>")
def func2(dft="sss"):
    return "el valor de dft es:"+ dft

if __name__=='__main__':
    app.run(debug=True)