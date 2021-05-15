from flask import render_template,redirect,request
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo



# @app.route("/dojos/<id>")
# def ninjas(id):
#     mysql = connectToMySQL('dojos_and_ninjas')
#     ninjas = mysql.query_db('SELECT * FROM ninjas;')
#     return render_template("index.html", all_ninjas = ninjas)



@app.route('/dojos/ninjas')
def new():
    
    return render_template("index_add.html", all_dojos = Dojo.all_dojos())


@app.route("/add_ninja", methods=['POST'])
def add_ninja():
    Ninja.add(request.form)
    return redirect('/dojos')