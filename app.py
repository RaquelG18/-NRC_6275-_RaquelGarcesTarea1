# Se importan las librerias necesarias para trabajar con el framwork Flask
from flask import Flask, render_template


# Se crea la aplicación, y se pasa como parametro el nombre de la aplicacion y el nombre de la carpeta donde se encuentra el archivo html
app = Flask(__name__, template_folder='templates')

# Se crea la ruta para la pagina principal o index
@app.route('/')
def index():
    # Retorna el archivo index.html o pag principal
    return render_template('index.html')


# Ejecutar la aplicación en modo debug e
if __name__ == '__main__':
    app.run(debug=True)
