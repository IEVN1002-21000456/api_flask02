from flask import Flask, render_template,request
from flask import make_response,jsonify,json
import forms

app = Flask(__name__)

@app.route('/index')
def index():
    titulo = "Pagina de incio"
    listado =['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/Pizzerialup',methods=['GET', 'POST'])
def Pizzerialup():
    nombre_cli = ""
    direccion_cli = ""
    telefono_cli = ""
    fecha_cli = ""
    pizzas_pedido = []
    ventas_totales = []
    total_pedido = 0
    mensaje_confirmacion = ""
    mostrar_ventas = False
    
    precios = {'Chica': 40, 'Mediana': 80, 'Grande': 120}
    precios_ingredientes = {'Jamon': 10, 'Piña': 10, 'Champiñones': 10}
    
    if request.method == 'POST':
       
        pizzas_str = request.cookies.get("pizzas_temp")
        if pizzas_str:
            pizzas_pedido = json.loads(pizzas_str)
        
        ventas_str = request.cookies.get("cookie_ventas")
        if ventas_str:
            ventas_totales = json.loads(ventas_str)
        
        if request.form.get("btnAgregar") == 'agregar':
            nombre_cli = request.form.get('nombre_cliente', '').strip()
            direccion_cli = request.form.get('direccion', '').strip()
            telefono_cli = request.form.get('telefono', '').strip()
            
            
            from datetime import datetime
            fecha_cli = datetime.now().strftime('%d-%m-%Y')
            
            tamano = request.form.get('tamano', '')
            numero = int(request.form.get('numero_pizzas', 1))
            
          
            ingredientes = []
            costo_ingredientes = 0
            if request.form.get('ing_jamon'):
                ingredientes.append('Jamon')
                costo_ingredientes += precios_ingredientes['Jamon']
            if request.form.get('ing_pina'):
                ingredientes.append('Piña')
                costo_ingredientes += precios_ingredientes['Piña']
            if request.form.get('ing_champinones'):
                ingredientes.append('Champiñones')
                costo_ingredientes += precios_ingredientes['Champiñones']
            
            ingredientes_str = ', '.join(ingredientes) if ingredientes else 'Ninguno'
            
            if nombre_cli and direccion_cli and telefono_cli and tamano:
                precio_base = precios.get(tamano, 0)
                subtotal = (precio_base + costo_ingredientes) * numero
                
                pizza_data = {
                    'nombre_cliente': nombre_cli,
                    'direccion': direccion_cli,
                    'telefono': telefono_cli,
                    'fecha': fecha_cli,
                    'tamano': tamano,
                    'ingredientes': ingredientes_str,
                    'numero_pizzas': numero,
                    'subtotal': subtotal
                }
                pizzas_pedido.append(pizza_data)
        
        elif request.form.get("btnQuitar") == 'quitar':
            if pizzas_pedido:
                pizzas_pedido.pop()
        
        elif request.form.get("btnTerminar") == 'terminar':
            if pizzas_pedido:
                total_pedido = sum(p['subtotal'] for p in pizzas_pedido)
                
                venta = {
                    'nombre': pizzas_pedido[0]['nombre_cliente'],
                    'direccion': pizzas_pedido[0]['direccion'],
                    'telefono': pizzas_pedido[0]['telefono'],
                    'fecha': pizzas_pedido[0]['fecha'],
                    'total': total_pedido
                }
                ventas_totales.append(venta)
                
                mensaje_confirmacion = f"Pedido confirmado. Total a pagar: ${total_pedido}"
                
                pizzas_pedido = []
                
                response = make_response(render_template('Pizzerialup.html',
                    pizzas=[],
                    mensaje=mensaje_confirmacion,
                    mostrar_ventas=False,
                    ventas=ventas_totales,
                    nombre_cli='',
                    direccion_cli='',
                    telefono_cli='',
                    fecha_cli=''))
                
                response.set_cookie('cookie_ventas', json.dumps(ventas_totales))
                response.delete_cookie('pizzas_temp')
                return response
        
       
        elif request.form.get("btnVentas") == 'ventas':
            mostrar_ventas = True
            pass
    
    if pizzas_pedido:
        nombre_cli = pizzas_pedido[0].get('nombre_cliente', '')
        direccion_cli = pizzas_pedido[0].get('direccion', '')
        telefono_cli = pizzas_pedido[0].get('telefono', '')
        fecha_cli = pizzas_pedido[0].get('fecha', '')
    
    response = make_response(render_template('Pizzerialup.html',
        pizzas=pizzas_pedido,
        nombre_cli=nombre_cli,
        direccion_cli=direccion_cli,
        telefono_cli=telefono_cli,
        fecha_cli=fecha_cli,
        mensaje=mensaje_confirmacion,
        ventas=ventas_totales,
        mostrar_ventas=mostrar_ventas))
    
    if request.method == 'POST' and not request.form.get("btnTerminar"):
        response.set_cookie('pizzas_temp', json.dumps(pizzas_pedido))
    
    return response


 
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
  tem=[]
  estudiantes=[]
  datos={}

  alumno_clas=forms.Userform(request.form)
  if request.method == 'POST' and alumno_clas.validate():

    if request.form.get("btnElimina")=='eliminar':
            response = make_response(render_template('Alumnos.html',))
            response.delete_cookie('usuario')

    mat=alumno_clas.matricula.data
    nom=alumno_clas.nombre.data
    ape=alumno_clas.apellido.data
    email=alumno_clas.correo.data

    datos={'matricula':mat,'nombre':nom.rstrip(),
            'apellido':ape.rstrip(),'email':email.rstrip()}  
    data_str = request.cookies.get("usuario")
    if not data_str:
        return "No hay cookie guardada", 404
    estudiantes = json.loads(data_str)
    estudiantes.append(datos)  
  response=make_response(render_template('Alumnos.html',
            form=alumno_clas, mat=mat, nom=nom, apell=ape, email=email))

  if request.method!='GET':
    response.set_cookie('usuario',json.dumps(estudiantes))
  return response

@app.route("/get_cookie")
def get_cookie():
     
    data_str = request.cookies.get("usuario")
    if not data_str:
        return "No hay cookie guardada", 404
 
    estudiantes = json.loads(data_str)
 
    return jsonify(estudiantes)
  



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