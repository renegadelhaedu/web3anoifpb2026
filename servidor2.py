#exemplo feito em sala no dia 08 04
from flask import *

app = Flask(__name__)

usuarios = []
#quando nao tem método explicito, considera-se que é método get
@app.route('/')
def inicial():
    return render_template('rene.html')


@app.route('/cadastrar' , methods=['POST'])
def fazercadastro():
    nome = request.form.get('nome')
    login = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')
    usuarios.append([nome,login,senha])
    texto = 'usuario cadastrado com sucesso!'

    return render_template('rene.html', mensagem=texto)


@app.route('/login')
def login():
    login = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')
    logado = False
    for u in usuarios:
        if login == u[1] and senha == u[2]:
            logado = True
            break
    if logado:
        return render_template('logado.html')
    else:
        texto = 'login ou senha incorretos'
        return render_template('index.html' , msg = texto)


app.run()
