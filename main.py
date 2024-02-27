from flask import Flask, render_template, request, url_for, redirect, session

import os
app = Flask("Magickmaker")

@app.route('/')
def index():
  # variable qui servira a contenir les infos de la bdd
  manganimes = []
  # titre du manganime : titre
  # image du manganime : url_image
  # lien du manganime : url_manganime
  return render_template("index.html", manganimes=manganimes)

@app.route('/mangas')
def mangas():
  return render_template("mangas.html")

@app.route('/animes')
def animes():
  return render_template("animes.html")

@app.route('/manganime')
def manganime():
  
  return render_template("manganime.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/register')
def register():
  return render_template("register.html")

@app.route('/add')
def add():
  return render_template("add.html")

@app.route('/admin')
def admin():
  return render_template("admin.html")

app.run(host='0.0.0.0', port=81)
