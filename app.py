from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def load_page():
	return render_template("index.html")

	
def home_page():

	fortunes = ["You will marry a wealthy person from a foreign land", 
	"You will have 10 children",
	"Your greatest desire shall come true on June 1, 2022",
	"You will travel to many countries"]

 
	return random.choice(fortunes)

# @app.route("/ran")
# def ran():
# 	san=["hala","roaa","soha"]
# 	ran = ["You will marry a wealthy person from a foreign land", 
# 	"You will have 10 children",
# 	"Your greatest desire shall come true on June 1, 2022",
# 	"You will travel to many countries"]
# 	return  render_template("index.html",san=random.choice(san))


@app.route("/ran")
def about():
	return  render_template("anew.html")


@app.route("/hla")
def hla():
	return render_template("index.html")


@app.route("/contact")
def contact():
	return  render_template("contact.html")

@app.route("/form_request",methods=['POST'])
def form_request():
	user_firstname=request.form["firstname"]
	
	user_lastname=request.form["lastname"]
	
	user_message=request.form["message"]

	#return 	  user_firstname+" "+user_lastname+" "+user_message
	return render_template("from_data.html",firstname=user_firstname,lastname=user_lastname,message=user_message)

if __name__ == "__main__":
	app.run()