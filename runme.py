from flask import Flask, render_template

app = Flask(__name__)

#http://127.0.0.1:5000/ = homepage
@app.route('/')
def index():
	return render_template("home.html")
	
if __name__ == "__main__":
	app.run()