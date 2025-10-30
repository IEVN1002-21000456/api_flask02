from flask import Flask, render_template,request
import forms

app = Flask(__name__)

@app.route('/index')
def index():
    titulo = "Pagina de incio"
    listado =['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template('index.html', titulo=titulo, listado=listado)
 
@app.route('/calculos', methods=['GET','POST'])
def calculo():
  if request.method == 'POST':
    numero1 = request.form['numero1']
    numero2 = request.form['numero2']
    opcin = request.form['operacion']
    if opcin =='suma':
      res = int(numero1) + int(numero2)
    if opcin == 'resta':
      res = int(numero1) - int(numero2)
    if opcin == 'multiplicacion':
      res = int(numero1) * int(numero2)
    if opcin == 'division':
      res = int(numero1) / int(numero2)
    return render_template('calculos.html', res=res, numero1=numero1, numero2=numero2)
  
  return render_template('calculos.html')

@app.route('/distancia', methods=['GET','POST'])
def distancia():
  if request.method =='POST':
    X1 = request.form['X1']
    Y1 = request.form['Y1']
    X2 = request.form['X2']
    Y2 = request.form['Y2']


    cal = Math.sqrt(Math.pow(int(X2) - int(X1),2) + Math.pow(int (Y2) - int(Y1), 2))
    return render_template('distancia.html', cal=cal, X1=X1, X2=X2, Y1=Y1, Y2=Y2)

  return render_template('distancia.html')
 
@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
  mat=0
  nom=""
  ape=""
  email=""

  alumno_clas=forms.Userform(request.form)
  if request.method == 'POST' and alumno_clas.validate():
    mat=alumno_clas.matricula.data
    nom=alumno_clas.nombre.data
    ape=alumno_clas.apellido.data
    email=alumno_clas.correo.data

  return render_template('Alumnos.html', form=alumno_clas, mat=mat, nom=nom, ape=ape,email=email)



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