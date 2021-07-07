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

empresa="Empresa test"
geologo="Geologo test"

@app.route("/rmr")
def rmr():
    return render_template('rmr.html', empresa=empresa, geologo=geologo)

@app.route("/mrmr", methods=['GET','POST'])
def mrmr():
    return render_template('mrmr.html')

@app.route('/rec_mrmr', methods=['GET','POST'])
def rec_mrmr():
    if request.method=='POST':
        ola=2
    info=[ola]
    return render_template('rec_mrmr.html', info=info)

@app.route('/rec_rmr', methods=['GET','POST'])
def rec_rmr():
    if request.method=='POST':
        resistencia=0
        r1=request.form.get("resistencia1")
        r2=request.args.get("resistencia2")
        if r1==None:
            resistencia=int(r2)
        elif r2==None:
            resistencia=int(r1)
        vida=int(request.form.get("vida"))
        uso=int(request.form.get("uso"))
        rqd=int(request.form.get("rqd"))
        separacion=int(request.form.get("separacion"))
        persistencia=int(request.form.get("persistencia"))
        abertura=int(request.form.get("abertura"))
        agua=0
        a1=request.form.get("agua1")
        a2=request.form.get("agua2")
        a3=request.form.get("agua3")
        if a1==None and a2==None:
            agua=int(a3)
        elif a1==None and a3==None:
            agua=int(a2)
        elif a2==None and a3==None:
            agua=int(a1)
        correccion=int(request.form.get("correccion"))
        rugosidad=int(request.form.get("rugosidad"))
        relleno=int(request.form.get("relleno"))
        alteracion=int(request.form.get("alteracion"))
    puntaje=resistencia+rqd+separacion+persistencia+abertura+agua+rugosidad+relleno+alteracion+correccion
    clase=""
    if puntaje < 21:
        clase="Clase V"
    elif puntaje < 41 and puntaje > 20:
        clase="Clase IV"
    elif puntaje < 61 and puntaje > 40:
        clase="Clase III"
    elif puntaje > 60 and puntaje < 81:
        clase="Clase II"
    elif puntaje > 80:
        clase="Clase I"
    
    excavacion=""
    apernado=""
    hormigon=""
    aceros=""
    if clase=="Clase I":
        excavacion="Frente completa, 3 metros de avance"
        apernado="Generalmente no requiere soporte"
        hormigon="Generalmente no requiere soporte"
        aceros="Generalmente no requiere soporte"
    elif clase=="Clase II":
        excavacion="Frente completa, 1 a 1,5 metros de avances, soporte completo a 20 metros de la frente"
        apernado="Localmente, apernado en corona de 3 metros de largo, espaciado 2,5 metros con mallado de alambre en el techo"
        hormigon="50 milimetros en corona, donde sea requerido"
        aceros="Ninguno"
    elif clase=="Clase III":
        excavacion="Encabezado superior y banco. Avance de 1,5 a 3 metros, comenzar soporte después de cada tronada. Soporte completo a 10 metros de la frente"
        apernado="Apernado sistemático de 4 metros de largo, espaciado de 1,5 a 2 metros en coronas y murallas, con mallado de alambre"
        hormigon="50 a 100 milimetros en frente y 30 milimetros lados"
        aceros="Ninguno"
    elif clase=="Clase IV":
        excavacion="Encabezado superior y banco, avance de 1 a 1,5 metros en corona. Instalar soporte al mismo tiempo que se genera excavación a 10 metros de la frente"
        apernado="Apernado sistemático de 4 a 5 metros de longitud, espaciados de 1 a 1,5 metros en corona y murallas, con mallado de alambre"
        hormigon="100 a 150 milimetros en corona y 100 milimetros en lados"
        aceros="Costillas livianas a medias, espaciadas 1,5 metros donde se requiera"
    elif clase=="Clase V":
        excavacion="Múltiples desvios de 0,5 a 1,5 metros de avance en encabezado superior. Instalar soporte al mismo tiempo que se genera la excavación, hormigón proyectado tan pronto como sea posible después de la tronada"
        apernado="Apernado sistemático de 5 a 6 metros de longitud, espaciado de 1 a 1,5 metros en corona y murallas, con mallado de alambre y pernos invertidos"
        hormigon="150 a 200 milimetros en corona, 150 milimetros en lados y 50 milimetros sobre frente"
        aceros="Costillas medias a pesadas, espaciadas de 0,75 metros con revestimiento de acero y tablestacas si se requiere. Invertido cerrado"

    return render_template('rec_rmr.html', puntaje=puntaje, clase=clase, excavacion=excavacion, apernado=apernado,hormigon=hormigon,aceros=aceros)


@app.route("/nuevo_proyecto")
def proyecto():
    return render_template('proyecto.html', show_predictions_modal=True)



if __name__ == "__main__":
    app.run(debug=True)

conn.close()