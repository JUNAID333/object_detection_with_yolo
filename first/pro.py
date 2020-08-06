from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/shop')
def shop():
	return render_template('shop.html')


@app.route('/process')
def process():
	return render_template('process.html')


@app.route('/product')
def product():
	return render_template('product.html')


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8000)


