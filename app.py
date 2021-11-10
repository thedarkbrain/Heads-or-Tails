from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/')
def result():
    heads_or_tails = random.randint(1, 2)
    return render_template('result.html', heads_or_tails = heads_or_tails)