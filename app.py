from flask import Flask, redirect, url_for, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sqlite3 as sql

conn = sql.connect('database.db')
print ("Opened database successfully")

#conn.execute('CREATE TABLE empresa (id INTEGER PRIMARY KEY,name TEXT, addr TEXT, city TEXT, region TEXT, country TEXT, rut TEXT)')
#print ("Table created successfully")

#conn.execute('CREATE TABLE geologos (id INTEGER PRIMARY KEY,name TEXT, rut TEXT, empresa_id INTEGER, FOREIGN KEY (empresa_id) REFERENCES empresa)')
#print ("Table created successfully")

#conn.execute('CREATE TABLE proyectos (id INTEGER PRIMARY KEY, ubicacion TEXT, empresa_id INTEGER, geologo_id INTEGER, FOREIGN KEY (empresa_id) REFERENCES empresa, FOREIGN KEY (geologo_id) REFERENCES geologos)')
#print ("Table created successfully")


app = Flask(__name__)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    surname = TextField('Surname:', validators=[validators.required()])

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/nueva_empresa')
def nueva_empresa():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        name=request.form['name']
        rut=request.form['rut']
        direccion=request.form['direccion']
        ciudad=request.form['ciudad']
        region=request.form['region']
        pais=request.form['pais']

        if form.validate():
            flash('Hello: {} {}'.format(name))

        else:
            flash('Error: All Fields are Required')

    return render_template('empresa.html', form=form)

@app.route("/rmr")
def calculo():
    return render_template('rmr.html')

@app.route("/mrmr")
def calculo():
    return render_template('mrmr.html')

if __name__ == "__main__":
    app.run()

conn.close()