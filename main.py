from flask import Flask, render_template, request, url_for, redirect, session

import os
app = Flask("Magickmaker")

@app.route('/')
def index():
  return (Hello World)
app.run(host='0.0.0.0', port=81)
