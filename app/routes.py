from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():

    return render_template('main.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/medintake')
def medintake():
    return render_template('medintake.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')
