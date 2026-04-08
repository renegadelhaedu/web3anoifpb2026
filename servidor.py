#importar o flask para o projeto
from flask import *

#instanciar o objeto do servidor web flask
app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('eu.html')

#@app.route('/cadastrar', methods=['POST'])

#executar o servidor
app.run(host='0.0.0.0' , port=5007)
