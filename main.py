#! /bin/python3

import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    con = sqlite3.connect("dbsite.db")

    chan = con.execute("Select * from chan")
    chan_list = chan.fetchall()

    file = con.execute("Select * from file")
    file_list = file.fetchall()

    person = con.execute("Select * from person")
    person_list = person.fetchall()

    service = con.execute("Select * from service")
    service_list = service.fetchall()

    sites = con.execute("Select * from sites")
    sites_list = sites.fetchall()

    soc = con.execute("Select * from soc")
    soc_list = soc.fetchall()

    tech = con.execute("Select * from tech")
    tech_list = tech.fetchall()

    return render_template('index.html', chan_list=chan_list, file_list=file_list, person_list=person_list, sites_list=sites_list, service_list=service_list, soc_list=soc_list, tech_list=tech_list)

@app.route('/add', methods=['POST', 'GET'])
def ssh():
    if request.method == 'POST':
        table = str(request.form['table'])

        host = str(request.form['name'])
        host.replace("'", "")
        host.replace('"', '')

        b32 = str(request.form['b32'])
        b32.replace("'", "")
        b32.replace('"', '')

        discription = str(request.form['discription'])
        discription.replace("'", "")
        discription.replace('"', '')

        con = sqlite3.connect("dbsite.db")
        con.execute(f"INSERT INTO { table } VALUES ('{ host }', '{ b32 }', '{ discription }', 0, 0, 'new')")
        con.commit()

        return render_template('successful.html')
    else:
        return render_template('add.html')

if __name__ == "__main__":
    app.run()
