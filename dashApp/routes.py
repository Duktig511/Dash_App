from dashApp.app import app
from flask import url_for, redirect, flash
from flask import render_template, request


################################################
# Flask Routes
#################################################


@app.route("/",  methods=['GET', 'POST'])
def landing():

    #render_template("layout.html")
    return render_template("landing.html")


@app.route("/form",  methods=['GET', 'POST'])
def form():

    jump = request.form["selection"]
    return render_template(f'{jump}.html', title=jump)


@app.route("/visual_1",  methods=['GET', 'POST'])
def visual_1():

    return render_template("visual_1.html")


@app.route("/visual_2",  methods=['GET', 'POST'])
def visual_2():

    return render_template("visual_2.html")


@app.route("/visual_3",  methods=['GET', 'POST'])
def visual_3():

    return render_template("visual_3.html")


@app.route("/visual_4",  methods=['GET', 'POST'])
def visual_4():

    return render_template("visual_4.html")


@app.route("/comparisons",  methods=['GET', 'POST'])
def comparisons():

    return render_template("comparisons.html")


@app.route("/data",  methods=['GET', 'POST'])
def data():

    return render_template("data.html")

