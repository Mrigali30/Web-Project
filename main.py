from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')


@app.route('/index')
def index():
    global name
    name = request.args.get('user')
    return render_template('index.html', name=name)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/review')
def review():
	return render_template('review.html')

@app.route('/horror')
def horror():
	return render_template('horror.html')

@app.route('/romance')
def romance():
	return render_template('romance.html')

@app.route('/action')
def action():
	return render_template('action.html')

@app.route('/recomm')
def recomm():
	return render_template('recomm.html')

@app.route('/con')
def con():
	return render_template('con.html')



if __name__ == '__main__':
    app.run(debug=True)