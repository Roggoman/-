from flask import Flask, url_for, render_template
from flask import request
app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Домашняя страница')

@app.route('/training/<prof>')
def train(prof):
    flag = True if "инженер" in prof or "строитель" in prof else False
    return render_template('training.html', title=prof, flag=flag)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
