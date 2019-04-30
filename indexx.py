
from bottle import route, run, HTTPResponse, template, request, get, redirect
from pymongo import MongoClient
import json, requests
from bottle.ext.mongo import MongoPlugin

from bson.json_util import dumps
username =''

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
    global username
    username = request.forms.get('studentID')
    password = request.forms.get('password')
    username2 = username
    print('This is username2', username2)
    enteredUser = db.students.find_one({"login" :{"studentID": username, "password": password}})
    enteredUser2 = db.teacher.find_one({"login" :{"teacherID": username, "password": password}})
    print(enteredUser)
    print(enteredUser2)
    #check if the user was found as a student, or teacher
    if enteredUser is not None :
    #if check_login(username, password):
        return "<p>Your login information was correct.</p>", redirect('/students')
    elif enteredUser2 is not None:
        return "<p>Your login information was correct.</p>", redirect('/teacher')
    else:
        return "<p>Login failed.</p>"
    
#@get('/login')
#def getusername():
 #   username = request.query.username
 #   print(username)

    
@route('/students')
def getstudents():
    username3= username
    print('This is username3', username3)
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

#Displays selected* class info and the student's assignments + grades
@route('/studentClassInfo/<classname>')
def studentClassInfo(classname):
    print(classname)
    db = client.gradebook # database gradebook
    classInfo = db.classes.find_one({"courseID": classname},{"teacher": 1, "courseTitle":1, "courseID":1})
    #need to show assignment info for that class
    #assignmentList = list(db.classes.find({"assignmentList" : {}}))
    assignmentInfo = list(db.assignments.find({"assignmentID": {'$regex':classname},"studentID":username}, {"studentID": 1, "assignmentID": 1, "grade": 1}))

    return template('show_classes', classes = classInfo, assignments = assignmentInfo)


## View teacher's classes and some info.
## when teacher logs in - they can view their classes
## and will be able to click on a class to view and edit assignments
@route('/teacher')
def teacherView():
    print(username)
    db = client.gradebook # database gradebook
    teachers = list(db.teacher.find({"teacherID": username},{'_id': 0}))
    #print(teachers)

    if teachers:
        return template('show_teachers', teachers=teachers)
    else: 
        return HTTPResponse(status=204)




#Displays selected* class info and the student's assignments + grades
@route('/classList')
def classList():
    db = client.gradebook # database gradebook
    classInfo = db.classes.find_one({"courseID": "Chem201-01-F2018"},{"teacher": 1, "courseTitle":1, "courseID":1})
    #need to show assignment info for that class
    classList =db.classes.find({"classList":{}},{})
    #assignmentList = list(db.classes.find({"assignmentList" : {}}))
    #assignmentInfo = list(db.assignments.find({"studentID":username}, {"studentID": 1, "assignmentID": 1, "grade": 1}))
    for entry in classList:
        print(classList)

    #return template('show_classList', classes = classInfo, classList = classList)
    
    
    

run(host='localhost', port=8080, debug=True)