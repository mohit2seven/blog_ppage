from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_Page():
    return render_template('index.html')
@app.route('/about')
def About_Page():
    state='Bihar'
    return render_template('about.html',state=state)

app.run(debug=True)