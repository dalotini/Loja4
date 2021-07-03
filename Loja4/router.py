from classes import pyodbc
from flask import Flask, redirect, url_for, request, render_template
from classes.colaboradorconnector import ColaboradorConnector
from classes.clienteconnector import ClienteConnector
import json 

app=Flask(__name__)

@app.route('/', methods = ['GET'])
def entrada():
    return render_template('index.html', msg='')

@app.route('/failure/<msg>')
def failure(msg):
    return render_template('index.html',msg=msg)

@app.route('/success/<username>')
def success(username):
    cliente=ClienteConnector()
    result=cliente.consultarTodosOsClientes(username)
    result=str(result)[3:-5]
    result=result.replace("', ), ('","")
    print(result)
    # username = username é o que definimos no HTML e o outro é Param da própria Func sql
    return render_template('dashboard.html',todososclientes=json.loads(result), username=username)



@app.route('/novapassword', methods = ['POST'])
def novapassword():
    username=request.form['username']
    password1=request.form['password1']
    password2=request.form['password2']

    colaborador=ColaboradorConnector()
    result=colaborador.novaPassword(username,password1,password2)
    if result[0][0]==0:
        return render_template('index.html', msg='')
    else:
        return render_template('mensagem.html',msg=result[0][2])


@app.route('/mostrarnovapassword/<username>', methods = ['GET'])
def mostrarnovapassword(username):
    return render_template('novapassword.html', username=username)


@app.route('/mostrarrecuperarpassword', methods = ['GET'])
def mostrarrecuperarpassword():
    return render_template('recuperarpassword.html')

@app.route('/recuperarpassword', methods = ['POST'])
def recuperarpassword():
    email=request.form['email']
    colaborador=ColaboradorConnector()
    result=colaborador.recuperarPassword(email)
   
    return render_template('mensagem.html', msg=result[0][1])

@app.route('/removercliente', methods= ['POST'])
def removercliente():
    username=request.form['username']
    numerocliente=request.form['numerocliente2']

    cliente=ClienteConnector()
    result=cliente.removerCliente(username,numerocliente)

    return redirect(url_for('success', username=username))

@app.route('/search',methods = ['POST'])
def search():
    username=request.form['username']
    search=request.form['search']
    cliente=ClienteConnector()

    result=cliente.search(username,search)
    result=str(result)[3:-5]
    result=result.replace("', ), ('","")
    return render_template('dashboard.html',todososclientes=json.loads(result),username=username)


@app.route('/registarcolaborador', methods=['POST'])
def registarcolaborador():
    username=request.form['username']
    nomecolaborador=request.form['nomecolaborador']
    nomeutilizador=request.form['nomeutilizador']
    palavrachave=request.form['palavrachave']
    telefone=request.form['telefone']
    email=request.form['email']

    colaborador=ColaboradorConnector()
    result= colaborador.registarColaborador(username,nomecolaborador,nomeutilizador,palavrachave,telefone,email)

    return redirect(url_for('success',username=username))

@app.route('/inserircliente', methods= ['POST'])
def inserircliente():
# n é preciso nmr de cliente aqui neste
    username=request.form['username']
    tipocliente=request.form['TipoCliente3']
    nome=request.form['Nome3']
    nif=request.form['NIF3']
    morada=request.form['Morada3']
    codigopostal=request.form['CodigoPostal3']
    telefone=request.form['Telefone3']
    email=request.form['email3']

    cliente=ClienteConnector()
    result=cliente.inserirCliente(username,tipocliente,nome,nif,morada,codigopostal,telefone,email)

    return redirect(url_for('success',username=username))


@app.route('/atualizarcliente', methods= ['POST'])
def atualizarcliente():
    username=request.form['username']
    numerocliente=request.form['numerocliente']
    tipocliente=request.form['TipoCliente']
    nome=request.form['Nome']
    nif=request.form['NIF']
    morada=request.form['Morada']
    codigopostal=request.form['CodigoPostal']
    telefone=request.form['Telefone']
    email=request.form['email']

    cliente=ClienteConnector()
    result=cliente.atualizarCliente(username,numerocliente,tipocliente,nome,nif,morada,codigopostal,telefone,email)

    return redirect(url_for('success', username=username))

@app.route('/login', methods = ['POST'])
def login():
    user=request.form['username']
    pwd=request.form['password']

    colaborador=ColaboradorConnector()
    result=colaborador.login(user,pwd)

    if result[0][0]==0:
        return redirect(url_for('success', username=result[0][1], msg=''))
    else:
        return redirect(url_for('failure',msg='Os dados não estão correctos.'))

@app.route('/logout', methods = ['POST'])
def logout():
    username=request.form['username']

    colaborador=ColaboradorConnector()
    result=colaborador.logout(username)

    return render_template('index.html', msg='')


if __name__ == '__main__':
   app.run(host="www.loja4.pt",port=80,debug = True)
   