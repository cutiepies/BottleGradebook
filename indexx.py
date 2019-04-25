
from bottle import route, run, HTTPResponse, template, request, get, redirect
from pymongo import MongoClient
import json, requests
from bottle.ext.mongo import MongoPlugin

from bson.json_util import dumps
##username =''
client = MongoClient('mongodb+srv://user:user123@cluster0-7i1kc.mongodb.net/test?retryWrites=true')
@route('/login') # or @route('/login')
def login():
    return 'Welcome to Gradebook. Please login with your studentID to proceed!''''
    <form action="/login" method="post">
            StudentID: <input name="studentID" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
        '''
@route('/login', method='POST') #@post('/login') # or 
def do_login():
    db = client.gradebook
    username = request.forms.get('studentID')
    password = request.forms.get('password')
    username2 = username
    print('This is username2', username2)
    enteredUser = db.students.find_one({"login" :{"studentID": username, "password": password}})
    print(enteredUser)
    if enteredUser is not None :
    #if check_login(username, password):
        return "<p>Your login information was correct.</p>", redirect('/students'), username2
    else:
        return "<p>Login failed.</p>"
    
#@get('/login')
#def getusername():
 #   username = request.query.username
 #   print(username)

    
@route('/students')
def getstudents():
    username3= do_login()
    print(username3)
#@get('/login')
    
    db = client.gradebook
    students = list(db.students.find({'studentID':username3}, {'_id': 0}))

    if students:


        return template('show_students', students=students)
    else: 
        return HTTPResponse(status=204)
        #return json.dumps(students)
 #   else: 
 #       raise HTTPResponse(status=204)
@route('/assignments')    
def getassignments():

    db = client.gradebook
    asn = list(db.assignments.find({}, {'_id': 0}))

    if asn:
                return template('show_assignments', assignments=asn)
    else: 
        return HTTPResponse(status=204)

 #       return json.dumps(asn)
   # else: 
 #       raise HTTPResponse(status=204)
 
@route('/grades')
def getgrades():
    db = client.gradebook
    grades = list(db.assignments.find({}, {'grades': 0}))
   
    
    
    
    if grades:
            return template('show_grades', assignments = grades)
    else:
            return HTTPResponse(status=204)
        
@route("/user/<username>")
def user_profile(username):
    user = mongo.db.users.find_one_or_404({"_id": username})
    return template('user_profile',
        user=user)

@route('/test')
def testSearchAssignmentGrades():
    db = client.gradebook # database gradebook
    #need to pass username into here to get the username/studentID for the assignments
    grades = list(db.assignments.find({'studentID'}))#'studentID':'ak7221os'}))
    return template('show_assignments', assignments = grades)


@route('/studentClassInfo')
def studentClassInfo():
    db = client.gradebook # database gradebook
    classInfo = db.classes.find_one({"courseID": "Chem201-01-F2018"},{"teacher": 1, "courseTitle":1, "courseID":1})
    #need to show assignment info for that class
    assignmentList = list(db.classes.find({"assignmentList" : {}}))
    assignmentInfo = list(db.assignments.find({}, {"studentID": 1, "assignmentID": 1, "grade": 1}))
    print(classInfo)
    print(assignmentList)
    print(assignmentInfo)
    return template('show_classes', classes = classInfo, assignments = assignmentInfo)



@route('/teacher')
def testtest():

    db = client.gradebook # database gradebook
    classes = list(db.teacher.find({"teacherID": "mm1234"},{"teacherID": 1, "name":1, "classes":1}))
    print(classes)

    #return template('show_assignments', assignments = grades)
def checklogin(username, password):
    
    print(username)
    
    

run(host='localhost', port=8080, debug=True)