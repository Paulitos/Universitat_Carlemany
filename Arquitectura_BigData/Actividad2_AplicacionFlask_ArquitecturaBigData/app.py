from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Variable global para almacenar el nombre del usuario
nombre_usuario = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global nombre_usuario
    if request.method == 'POST':
        nombre_usuario = request.form.get('nombreUsuario', None)
        return redirect(url_for('contenido'))
    return render_template('index.html')

@app.route('/contenido')
def contenido():
    global nombre_usuario
    if not nombre_usuario:
        return render_template('error.html', mensaje="No puedo mostrarte el contenido, sin saber quién eres. Por favor entra tu nombre en ", enlace=url_for('index'))
    else:
        return render_template('contenido.html', nombre=nombre_usuario)

if __name__ == '__main__':
    app.run(debug=True)


'''
@app.route('/bienvenida/<nombre>')
def bienvenida(nombre):
    return render_template('bienvenida.html', nombre=nombre)
'''