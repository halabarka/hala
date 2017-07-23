from flask import Flask, render_template, request
import random
#import dataset

# db=dataset.connect( "postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4") 
# table=db["hala_user"]
# table.insert(dict(name="hala barka",age = 16))
# table.insert(dict(name="renan saed",age = 15))
# table.insert(dict(name="khaled zaqout",age = 14))

# for hala_user in table:
# 	print ("id :"+ str(hala_user["id"])+"name:"+hala_user["name"]+"age:"+str(hala_user["age"]))

 
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
	return render_template("from_data.html",firstname=user_firstname,lastname=user_lastname,message=user_message)

#	return table.find_one( firstname="apple")



if __name__ == "__main__":
	#print (db.tables)

	#print (table.columns)
	app.run()
