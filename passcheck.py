from flask import Flask, render_template, url_for, request
from forms import PasswordForm
import searchpass
app = Flask(__name__)

app.config['SECRET_KEY'] = '15253fe70fb35e351631b47aeb9165e5' # secrets.token_hex(16)

@app.route("/", methods=['GET','POST'])
def index():
    form = PasswordForm()
    return render_template('index.html', form=form)

@app.route("/result", methods=['POST'])
def result():
   if request.method == 'POST':
        password = request.form['password']
        result = searchpass.checkpass(password)
        if result==True:
            return render_template("result_present.html")
        else:
            return render_template("result_absent.html")

if __name__ == "__main__":
    app.run(debug=True)
