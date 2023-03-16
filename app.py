from flask import redirect,Flask,render_template
from flask import request
from flask import url_for
import forms

from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.route('/',methods=['GET','POST'])
def index():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=create_form.nombre.data,
                     apellidos=create_form.apellidos.data,
                     email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
    return render_template('index.html',form=create_form)

@app.route("/ABCompleto",methods=['GET','POST'])
def ABCompleto():
    create_form=forms.UserForm(request.form)
    #select * from alumnos
    alumnos=Alumnos.query.all()
    return render_template('ABCompleto.html', form=create_form,alumnos=alumnos)

@app.route('/modificar',methods=['GET','POST'])
def modificar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #select * from alumnos where id == id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    if request.method=='POST':
        id=create_form.id.data
        #select * from alumnos where id == id
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre=create_form.nombre.data
        alum.apellidos=create_form.apellidos.data
        alum.email=create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('modificar.html',form=create_form)

@app.route('/eliminar',methods=['GET','POST'])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #select * from alumnos where id == id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    if request.method=='POST':
        id=create_form.id.data
        #select * from alumnos where id == id
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre=create_form.nombre.data
        alum.apellidos=create_form.apellidos.data
        alum.email=create_form.email.data
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('eliminar.html',form=create_form)

if __name__=='__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)