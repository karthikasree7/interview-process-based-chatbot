
from flask import Flask,request,url_for,redirect,flash,session
from flask import render_template
import json 
from service import *
from flask import *
from datetime import date 
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "abc"  

@app.route("/")
def index():
	return render_template("home.html") 

@app.route("/home.html")
def home():
	return render_template("home.html") 

@app.route("/userContact.html")
def userContact():
	return render_template("userContact.html")

@app.route("/about.html")
def about():
	return render_template("about.html") 

@app.route("/forgotPassword.html")
def frgtPassword():
	return render_template("forgotPassword.html") 


@app.route("/bot.html")
def bot():
	result=getinvaildquestion()
	return render_template("bot.html",data=result) 
	
@app.route("/technical_vid.html")
def techVideos():
	result=getValues("technical")
	return render_template("technical_vid.html",data=result)

@app.route("/aptitude_vid.html")
def aptiVideos():
	result=getValues("aptitude")
	return render_template("aptitude_vid.html",data=result)
	
@app.route("/interview_vid.html")
def interviewVideos():
	result=getValues("hr")
	return render_template("interview_vid.html",data=result)


@app.route("/chatbot.html")
def chatbot():
	return render_template("chatbot.html") 	

@app.route("/add_video.html")
def addVideo():
	return render_template("add_video.html")

@app.route("/contact.html")
def contact():
	return render_template("contact.html")

@app.route("/user_login.html")
def userLogin():
	return render_template("user_login.html") 

@app.route("/admin_login.html")
def adminLogin():
	return render_template("admin_login.html") 
	

@app.route("/register.html")
def registerHtml():
	return render_template("register.html") 
	
@app.route("/user.html")
def userPage():
	return render_template("user.html") 

@app.route("/admin.html")
def admin():
	return render_template("admin.html") 
	
@app.route("/aptitude_vid.html")
def apttVdo():
	return redirect("/aptitude_vid.html") 

@app.route("/technical_vid.html")
def techVdos():
	return redirect("/technical_vid.html") 

@app.route("/interview_vid.html")
def hrVdos():
	return redirect("/interview_vid.html") 

@app.route("/logout")
def logout():
	return redirect("/") 

@app.route("/add_interview.html")
def addInterview():
	print("---------render----")
	return render_template("/add_interview.html")

@app.route("/forgotpassword",methods=['POST','GET'])
def frgtPass():
	if request.method == "POST":
		aadhar=request.form['demo']
		email=request.form['email']
		mobile=request.form['mob']
		passwrd=showPassword(aadhar,email,mobile)
		print(passwrd)
		if(passwrd is None):
			return render_template("/forgotPassword.html",data='please enter valid Credentials')
		else:
			return render_template("/forgotPassword.html",data='your password is '+passwrd[0])

@app.route("/getchat")
def query_example():
	if request.method == "GET":
		msg = request.args.get('msg')
		username = session['username']
		data=getchat(msg, username)
		return json.dumps({'result':data});

@app.route("/interview_notif.html")
def interview_notif():
	print("---------render----")
	data=getInterest()
	return render_template("/interview_notif.html",data=data)

@app.route("/view_interview.html")
def viewinterview():
	if request.method == "GET":
		if 'role'  in session:
			role=session['role']
			username=session['username']
			data=getinterviewDetails(role,username);
			return render_template("/view_interview.html",data=data,role=role)
	return redirect("/")

@app.route("/register",methods=['POST','GET'])
def register():
	if request.method == "POST":		
		aadharNo=request.form['aadhar']		
		fName=request.form['fName']
		lName=request.form['lName']
		mobNumber=request.form['phone']
		email=request.form['email']
		password=request.form['password']
		techSkills=request.form['techSkills']			
		userRegister(aadharNo,fName,lName,mobNumber,email,password,techSkills)
	return redirect("/")

@app.route("/addInterview",methods=['POST','GET'])
def saveInterview():
	print("-----------------------------------------------")
	if request.method == "POST":	
		print("-----------------------------------------------")	
		cmpyName=request.form['cmpyName']		
		techSkills=request.form['techSkills']
		experience=request.form['experience']
		inLocation=request.form['inLocation']
		print(cmpyName,techSkills,experience,inLocation)			
		saveInterviewRest(cmpyName,techSkills,experience,inLocation)
	return redirect("/add_interview.html")


@app.route("/updateProfile",methods=['POST','GET'])
def updateProfile():
	if request.method == "POST":
		user_id=request.form['user_id']
		fName=request.form['fName']
		lName=request.form['lName']
		mobNumber=request.form['mobNumber']
		email=request.form['email']
		education =request.form['education']
		techSkills  =request.form['techSkills']
		dob =request.form['dob']
		gender =request.form['gender']
		userCity =request.form['userCity']
		userState =request.form['userState']
		userCountry  =request.form['userCountry']
		pinCode   =request.form['pinCode']
		updateUser(fName,lName,mobNumber,email,education,techSkills,dob,gender,userCity,userState,userCountry,pinCode,user_id)
	return redirect("/profile.html")

@app.route("/profile.html",methods=['POST','GET'])
def user():
	if request.method == "GET":
		if 'username' in session:
			user_name = session['username'];
			print(user_name)			
			data=getUser(user_name)
			return render_template("user_profile.html",data=data)
	return render_template("user_login.html")
	
	

@app.route("/intrested",methods=['POST','GET'])
def intrested():
	#print(request.method)
	if request.method == "POST":
		print("------------------------------enter-------------------")
		user_name = session['username']
		company=request.form['company']
		tech=request.form['tech']
		experience=request.form['experience']
		location=request.form['location']
		interest(user_name,company,tech,experience,location)	
		return redirect("/view_interview.html")
	return redirect("/")



@app.route("/login",methods=['POST','GET'])
def login():
	if request.method == "POST":
		username=request.form['username']
		passwrd=request.form['password']
		if username=="admin@gmail.com":
			if passwrd=="admin@gmail.com":
				session["user_id"]="admin@gmail.com"
				session["username"]="admin@gmaail.com"
				session["role"]="admin"
				return redirect("/admin.html")					
		result=getLogin(username,passwrd)
		if(len(result)>0):			
			session["userObj"]=result
			for x in result:
				print(x)
				session["user_id"]=x[0]
				session["username"]=x[1]
				session["role"]=x[4]
			return redirect("/user.html")
		
		return render_template("user_login.html",status="username or password is wrong")

@app.route("/StudentSave",methods=['POST','GET'])
def StudentSave():
	if request.method == "POST":
		name=request.form['name']
		degree=request.form['degree']
		phone=request.form['phone']
		address=request.form['address']
		stdSave(name,degree,phone,address)
	return render_template("index.html")
	
@app.route("/studentget",methods=['POST','GET'])
def studentget():
	result = None
	if request.method == "GET":
		result=getstudent()
	
	return json.dumps({'result':result});


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        category=request.form['vdoType']
        if 'file' not in request.files:
            flash('No file part')
            print("no files")
            return redirect("/add_video.html")
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            print("no filename")
            return redirect("/add_video.html")
        filename = secure_filename(file.filename)
        print(file.filename)
        if(category == 'aptVdo'):
            file.save(os.path.join('D:/project/interview/static/videos/Aptitude/', filename))
            aptVdo = aptVideo('aptitude', '/static/videos/Aptitude/'+filename, filename)
        elif(category == 'techVdo'):
            file.save(os.path.join('D:/project/interview/static/videos/Technical/', filename))
            techVdo = techVideo('technical', '/static/videos/Technical/'+filename, filename)
        elif(category == 'hrVdo'):
            file.save(os.path.join('D:/project/interview/static/videos/HR/', filename))
            hrVdo=hrVideo('hr', '/static/videos/HR/'+filename, filename)
        return redirect("/add_video.html")


@app.route("/newQues",methods=['POST','GET'])
def bot_answer():
	if request.method == "POST":
		username=request.form['username']
		question=request.form['question']
		#newQuesSave(username,question)
	return render_template("bot_answer.html",data=question)
	
@app.route("/insertQuestion",methods=['POST','GET'])
def insertQuestion():
	if request.method == "POST":
		answer=request.form['answer']
		question=request.form['question']
		newQuesSave(answer,question,date.today())
	return redirect("/bot.html")


@app.route("/invaildQus")
def addInvaild():
	if request.method == "GET":
		qus = request.args.get('question')
		username=session['username']
		if insertInvaild(qus,date.today(),username):
			return json.dumps({'result':True});
		return json.dumps({'result':False});

if __name__=="__main__":
	app.run(debug=True)
