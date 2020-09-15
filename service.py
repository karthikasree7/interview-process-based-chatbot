from connection import *



def stdSave(name,degree,phone,address):
	mycursor = conn.cursor()
	sql = "INSERT INTO student (name, degree,phone,address) VALUES (%s, %s, %s, %s)"
	val = (name,degree,phone,address)
	mycursor.execute(sql, val)
	conn.commit()


def interest(user_name,company,tech,experience,location):
	print("-----------------------------------------------------")
	print(user_name)
	print(company)
	mycursor = conn.cursor()
	sql = "INSERT INTO interview_nodification (username,companyname) VALUES (%s, %s)"
	val = (user_name,company)
	mycursor.execute(sql, val)
	conn.commit()
	
		
def getInterest():
	mycursor = conn.cursor()
	mycursor.execute("SELECT * FROM interview_nodification")
	myresult = mycursor.fetchall()
	return myresult
		
		
def getstudent():
	mycursor = conn.cursor()
	mycursor.execute("SELECT * FROM student")
	myresult = mycursor.fetchall()
	return myresult
	
def userRegister(aadhar,fName,lName,phone,email,password,techSkills):
	mycursor = conn.cursor()
	sql = "INSERT INTO userRegisteration (aadharNo,fName,lName,mobNumber,email,passwrd,techSkills) VALUES (%s, %s, %s, %s ,%s ,%s,%s)"
	val = (aadhar,fName,lName,phone,email,password,techSkills)
	mycursor.execute(sql, val)
	conn.commit()
	loginSave(email,password,"user","active")
	
	

def loginSave(email,password,uRole,status):
	mycursor = conn.cursor()
	sql = "INSERT INTO login (username,passwrd,uRole,status) VALUES (%s, %s, %s, %s)"
	val = (email,password,uRole,status)
	mycursor.execute(sql, val)
	conn.commit()
	
def getLogin(username,passwrd):
	mycursor = conn.cursor()
	query="SELECT * FROM login where username='"+username+"'  and passwrd='"+passwrd+"' "
	print(query)
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	#print("-------------------------"+myresult[0])
	#for x in myresult:
	#	print(x)  
	return myresult
	
def getUser(user_name):
	mycursor = conn.cursor()
	query="SELECT * FROM userRegisteration where email='"+user_name+"'"
	print(query)
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	#print("-------------------------"+myresult[0])
	#for x in myresult:
	#	print(x)  
	return myresult
	
	
def updateUser(fName,lName,mobNumber,email,education,techSkills,dob,gender,userCity,userState,userCountry,pinCode,user_id):
	mycursor = conn.cursor()
	query="update userregisteration set fName='"+fName+"', lName='"+lName+"', mobNumber='"+mobNumber+"',email='"+email+"', education='"+education+"', techSkills='"+techSkills+"', dob='"+dob+"',gender='"+gender+"', userCity='"+userCity+"', userState='"+userState+"', userCountry='"+userCountry+"', pinCode='"+pinCode+"' where id ='"+user_id+"'"
	print(query)
	mycursor.execute(query)
	
	
def saveInterviewRest(cmpyName,techSkills,experience,inLocation):
	
	mycursor = conn.cursor()
	sql = "insert into interview (cmpyName, techSkills, experience, inLocation) values ('"+cmpyName+"', '"+techSkills+"', '"+experience+"', '"+inLocation+"')"
	print(sql)
	mycursor.execute(sql)
	conn.commit()
	

def showPassword(aadhar,email,mobile):
	query=""
	mycursor=conn.cursor()
	query="select passwrd from userregisteration where aadharno='"+aadhar+"' and email='"+email+"' and mobnumber='"+mobile+"'"
	mycursor.execute(query)
	myresult = mycursor.fetchone()
	return myresult

def getchat(msg, username):
	query=""
	mycursor = conn.cursor()
	data = msg.lower()
	query="select answer from question where name like '%"+msg+"%'"
	mycursor.execute(query)
	myresult = mycursor.fetchone()
	return myresult

	
def getinterviewDetails(role,username):
	query=""
	mycursor = conn.cursor()
	if(role=="admin"):
		query="SELECT * FROM interview "
	else:
		print("-----------------------"+username)
		result=getUser(username)
		print(result)
		query="SELECT * FROM interview where techSkills like '%"+result[0][7]+"%' "
	
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	#print("-------------------------"+myresult[0])
	#for x in myresult:
	#	print(x)  
	return myresult
	
def aptVideo(category, filePath, filename):
	query =""
	mycursor = conn.cursor()
	query="insert into studyVideo (category, filePath, filename) values ('"+category+"', '"+filePath+"', '"+filename+"')"
	mycursor.execute(query)
	conn.commit()
	query = "select filepath,filename from studyVideo where category = '"+category+"'"
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	return myresult

def techVideo(category, filePath, filename):
	query =""
	mycursor = conn.cursor()
	query="insert into studyVideo (category, filepath, filename) values ('"+category+"', '"+filePath+"', '"+filename+"')"
	mycursor.execute(query)
	conn.commit()


def hrVideo(category, filePath, filename):
	query =""
	mycursor = conn.cursor()
	query="insert into studyVideo (category, filepath, filename) values ('"+category+"', '"+filePath+"', '"+filename+"')"
	mycursor.execute(query)
	conn.commit()
	query = "select filepath,filename from studyVideo where category = '"+category+"'"
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	return myresult
	
def getValues(category):
	mycursor = conn.cursor()
	query = "select filepath,filename from studyVideo where category='"+category+"'"
	print(query)
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	return myresult
	
def insertInvaild(qus,date,username):
	mycursor = conn.cursor()
	sql = "INSERT INTO invaildquestion (question,date,username) VALUES (%s, %s,%s)"
	val = (qus,date,username)
	mycursor.execute(sql, val)
	conn.commit()
	

def getinvaildquestion():
	mycursor = conn.cursor()
	query = "select * from invaildquestion"
	print(query)
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	return myresult
	
def newQuesSave(answer,name,date):
	mycursor = conn.cursor()
	sql = "INSERT INTO question (name,answer,date) VALUES (%s, %s,%s)"
	val = (name,answer,date)
	mycursor.execute(sql, val)
	conn.commit()
	
	
