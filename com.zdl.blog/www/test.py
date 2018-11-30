from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_from():
	return '''<form action="/signin" method="post">
			<p><input type="text" name="username" />
			<p><input type="password" name="password" />
			<p><input type="submit" name="submit" />
			<p></form>
			'''

@app.route('/signin',methods=['POST'])
def signin():
	if request.form['username'] =='admin' and request.form['password'] == '12345':
		return '<h3>Hello, admin!</h3>'
	return '<h3>Bad username or password.</h3>'

if (__name__ == '__main__'):
	app.run()