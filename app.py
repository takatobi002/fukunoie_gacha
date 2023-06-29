from flask import Flask, render_template
import os
import gacha
from jinja2 import escape

app = Flask(__name__)

@app.route('/')
def base():
    result_menu, money, budget = gacha.calculation()
    result_amount = money - budget
    return render_template('result.html', result_menu=result_menu, result_amount=result_amount)

@app.route('/result.html')
def result():
    result_menu, money, budget = gacha.calculation()
    result_amount = money - budget
    return render_template('result.html', result_menu=result_menu, result_amount=result_amount)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
