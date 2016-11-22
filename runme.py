from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

#Name of DB and link to it using username:password
#In this case everyone has same rights -> can split into admin/regular user with read only rights
app.config['MONGO_DBNAME'] = 'mongologin'
app.config['MONGO_URI'] = 'mongodb://Richard:dbpassword@ds159377.mlab.com:59377/mongologin'

mongo = PyMongo(app)

#http://127.0.0.1:5000/ = homepage
@app.route('/')
def index():
	return render_template('home.html')

#http://127.0.0.1:5000/irelia to poppy
#Change content of main-content div
@app.route('/irelia')
def irelia():
	return render_template('irelia.html')
	
@app.route('/jax')
def jax():
	return render_template('jax.html')
	
@app.route('/malphite')
def malphite():
	return render_template('malphite.html')
	
@app.route('/riven')
def riven():
	return render_template('riven.html')
	
@app.route('/singed')
def singed():
	return render_template('singed.html')
	
@app.route('/gnar')
def gnar():
	return render_template('gnar.html')
	
@app.route('/gangplank')
def gangplank():
	return render_template('gangplank.html')
	
@app.route('/poppy')
def poppy():
	return render_template('poppy.html')
	
#Profile, if theres a username saved in session - return profile.html
#Otherwise go to login.html which asks for login details
@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html')

    return render_template('login.html')
	
#Login, if the username exists in database then check if the correct password is entered
#On success, create session and redirect to profile
#Otherwise invalid information entered or the account does not exist
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
		#if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('profile'))

    return 'Invalid username/password combination'
	
#Register, if the method is post - check for username in database, if username does not exist then add the record to the database
#Password is hashed using bcrypt for security and the hashpass value is stored on the database instead of the password
#Session is then created and redirects user to profile
#If the method is get - return register.html
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('profile'))
        
        return 'That username already exists!'

    return render_template('register.html')
	
#about page
@app.route('/about')
def about():
	return render_template('about.html')
	
#playstyle page
@app.route('/playstyle')
def playstyle():
	return render_template('playstyle.html')
	
	
if __name__ == "__main__":
	app.secret_key = 'mysecret'
	app.run()