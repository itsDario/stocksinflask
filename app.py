from flask import Flask, render_template
from data import Stocks

Stocks = Stocks()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/stocks')
def stocks():
    return render_template('stocks.html', stocks=Stocks)


@app.route('/stock/<string:id>/')
def stock(id):
    return render_template('stock.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)
