from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    app.logger.debug("Inside home and loading home.html")
    app.logger.info(f"Working in the path { request.path}")
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es: {edad}'
    # En la instruccion de abajo se llama a un html con un parametro {{}} para el binding
    #return render_template(mostrar.html', nombre=nombre)

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_nombre(nombre):
    return f'Tu nombre es:{nombre}'

if __name__ == '__main__':
    app.run(debug=True)
