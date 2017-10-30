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



if __name__ == '__main__':
    app.run(debug=True)