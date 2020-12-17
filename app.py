from flask import Flask, render_template
import os
import gacha

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('hello.html')

@app.route('/hello.html')
def hello():
    return render_template('hello.html')

@app.route('/result.html')
def result():
    result_menu = gacha.result_menu()
    result_amount = gacha.result_amount()
    return render_template('result.html', result_menu=result_menu, result_amount=result_amount)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
