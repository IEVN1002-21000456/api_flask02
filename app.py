from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def home():
    titulo = "Pagina de incio"
    listado =['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template('index.html', titulo=titulo, listado=listado)
 
 
@app.route('/calculos')
def about():
  return render_template('calculos.html')

@app.route('/distancia')
def distancia():
  return render_template('distancia.html')
 
@app.route('/user/<string:user>')
def user(user):
  return f"Hola, {user}!"
 
 
@app.route("/numero/<int:num>")
def func(num):
  return f"El numero es: {num}"
 
 
@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
  return f"La suma es: {num1 + num2}"
 
 
@app.route("/user/<int:id>/<string:username>")
def username(id,username):
  return "ID: {} nombre: {}".format(id,username)
 
 
@app.route("/suma/<float:n1>/<float:n2>")
def func1(n1, n2):
  return "la suma es: {}".format(n1+n2)
 
@app.route("/default/")
@app.route("/default/<string:dft>")
def func2(dft="sss"):
  return "El valor de dft es: "+dft
 
@app.route("/prueba")
def func4():
  return '''
  <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <title>Pagina de prueba</title>
    </head>
      <body>
        <h1>hola esta es una pagina web</h1>
        <p>Esta es para probar el entorno de trabajo</p>
      </body>
    </html>
  '''
 
if __name__ == '__main__':
  app.run(debug=True)