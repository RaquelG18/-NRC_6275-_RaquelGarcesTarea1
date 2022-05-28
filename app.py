# Se importan las librerias necesarias para trabajar con el framwork Flask
from flask import Flask, render_template

# Se crea la aplicación con parámetro el nombre de la aplicación y el nombre de la carpeta donde se encuentra el archivo html
app = Flask(__name__, template_folder='templates')

# Se crea la ruta (/) 
@app.route('/')
#Se define la función de nombre principal para llamar el archivo index.html
def principal():
    # Retorna el archivo index.html o pag principal
    return render_template('index.html')


# Menú para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
