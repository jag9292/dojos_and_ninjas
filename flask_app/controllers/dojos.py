from flask import render_template,redirect,request
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/dojos")
def dojos():
    mysql = connectToMySQL('dojos_and_ninjas')
    dojos = mysql.query_db('SELECT * FROM dojos;')
    return render_template("index.html", all_dojos = dojos)

@app.route("/dojos", methods=['POST'])
def add_dojo():
    Dojo.add(request.form)
    return redirect("/dojos")

@app.route("/dojos/<id>")
def show_dojo(id):
    data = {
        'id' : int(id)
    }
    return render_template("index_show.html", dojo = Dojo.get_ninja_by_dojo(data))

