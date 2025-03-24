import os
from flask import Flask, render_template, request, redirect, url_for, flash
from config.config import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('auth/login.html')

@app.route('/login', methods=['POST'])
def login():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('home/dashboard.html')

@app.route('/view')
def view():
    return render_template('home/view.html')

@app.route('/update')
def update():
    return render_template('home/update.html')

@app.route('/delete')
def delete():
    return render_template('home/delete.html')

@app.route('/add' )
def add():
    return render_template('home/add.html')

@app.route('/401')
def unauthorized():
    return render_template('errors/401.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(host  = '0.0.0.0', port = 5000)