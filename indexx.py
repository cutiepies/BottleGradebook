
from bottle import route, run, HTTPResponse, template, request, get, redirect, static_file
from pymongo import MongoClient
import json, requests, math
from bottle.ext.mongo import MongoPlugin

from bson.json_util import dumps
username =''

client = MongoClient('mongodb+srv://user:user123@cluster0-7i1kc.mongodb.net/test?retryWrites=true')
#apply css statically
@route('/css/<filepath>')
def server_static(filepath):
    return static_file(filepath, root='/static/css')

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

@route('/grades')
def getgrades():
    db = client.gradebook
    grades = list(db.assignments.find({}, {'grades': 0}))
    if grades:
            return template('show_grades', assignments = grades)
    else:
            return HTTPResponse(status=204)


#Displays selected* class info and the student's assignments + grades
@route('/studentClassInfo/<classname>')
def studentClassInfo(classname):
    print(classname)
    db = client.gradebook # database gradebook
    classInfo = db.classes.find_one({"courseID": classname},{"teacher": 1, "courseTitle":1, "courseID":1})
    #need to show assignment info for that class
    #assignmentList = list(db.classes.find({"assignmentList" : {}}))
    assignmentInfo = list(db.assignments.find({"assignmentID": {'$regex':classname},"studentID":username}, {"studentID": 1, "assignmentID": 1, "grade": 1}))
    #print(assignmentInfo)

    allGrades= list(db.assignments.find({"assignmentID": {'$regex':classname},"studentID":username}, {"_id":0, "grade": 1}))
    #print("allgrades: ",allGrades)

    #for entries in allGrades:
    totalGrade = sum(item['grade'] for item in allGrades)
    val = len(allGrades)
    avgGrade =totalGrade/val
    #print(totalGrade)
    #print(avgGrade)

    return template('show_classes', avgGrade=avgGrade, classes = classInfo, assignments = assignmentInfo)


## View teacher's classes and some info.
## when teacher logs in - they can view their classes
## and will be able to click on a class to view and edit assignments
@route('/teacher')
def teacherView():
    print(username)
    db = client.gradebook # database gradebook
    teachers = list(db.teacher.find({"teacherID": username},{'_id': 0}))
    if teachers:
        return template('show_teachers', teachers=teachers)
    else:
        return HTTPResponse(status=204)




#Displays selected* class info and the student's assignments + grades
@route('/classList/<classname>')
def classList(classname):
    db = client.gradebook # database gradebook
    classInfo = db.classes.find_one({"courseID": classname},{"teacher": 1, "courseTitle":1, "courseID":1})
    #need to show assignment info for that class
    classList = list(db.classes.find({"courseID":classname},{"classList":1}))
    assignmentList = list(db.classes.find({"courseID":classname},{ "assignmentList": 1}))

    #Calculate class average grade
    allGrades= list(db.assignments.find({"assignmentID": {'$regex':classname}}, {"_id":0, "grade": 1}))
    #indexgrades = list(db.assignments.explain().find({"assignmentID": {'$regex':classname}}, {"_id":0, "grade": 1}))
    
    #print("allgrades: ",allGrades)
    #for entries in allGrades:
    totalGrade = sum(item['grade'] for item in allGrades)
    val = len(allGrades)
    avgGrade =totalGrade/val
    #print(totalGrade)
    #print(avgGrade)
    return template('show_classList', avgGrade=avgGrade, classes = classInfo, classList = classList, assignmentList = assignmentList, classname = classname)

# post method
@route('/createAssignment', method = 'POST')
def createAssignment(classname):

     classname2 = classList(classname)


     print(classname2)



#WORKS - teacher views assignments for specific student
#Displays selected* class info and the student's assignments + grades
@route('/teacherViewStudentAssignments/<classname>/<studentID>')
def teacherViewStudentAssignments(classname, studentID):
    print(classname)
    print(studentID)
    db = client.gradebook # database gradebook
    classInfo = db.classes.find_one({"courseID": classname},{"teacher": 1, "courseTitle":1, "courseID":1})
    #need to show assignment info for that class
    #assignmentList = list(db.classes.find({"assignmentList" : {}}))
    assignmentInfo = list(db.assignments.find({"assignmentID": {'$regex':classname},"studentID":studentID}, {"studentID": 1, "assignmentID": 1, "grade": 1}))
    #print(assignmentInfo)

    allGrades= list(db.assignments.find({"assignmentID": {'$regex':classname},"studentID": studentID}, {"_id":0, "grade": 1}))
    #print("allgrades: ",allGrades)

    #for entries in allGrades:
    totalGrade = sum(item['grade'] for item in allGrades)
    val = len(allGrades)
    avgGrade =totalGrade/val
    #print(totalGrade)
    #print(avgGrade)

    return template('show_classesTeacherView', avgGrade=avgGrade, classes = classInfo, assignments = assignmentInfo)

#WORKS!
#update grade - (ISSUE- since in for loop, only updates the last form item.. lol
#can give each a button or idk?
#but at least one edit works to demo.
@route('/update', method='POST') #@post('/login') # or
def updateGrades():
    db = client.gradebook
    studentID = request.forms.get('studentID')
    assignmentID =  request.forms.get('assignmentID')
    grade = request.forms.get('grade')
    
    #tried to use class name to allow reroute back to current class.. cant 
    classname = request.forms.get('classname')
    print('assignment: ', assignmentID)
    print('student: ', studentID)
    print('newgrade: ', grade)
    print('This is grade', grade)
    print('classname', classname)
    
    #stupid form makes grade string, need to convert back to int for database
    grade2 = int(grade)
    print(grade2)
    #then will want to edit database to reflect the changes... ik in for loop so maybe wont work
    ## updates document ##
    
    myquery = { "assignmentID":assignmentID,"studentID": studentID }
    newvalues = { "$set": { "grade": grade2 } }
    try:
        db.assignments.update_one(myquery, newvalues)
    except Exception as e:
        print ("insert failed:", e)
    
    
    return "<p>Your grades have been updated.</p>", redirect('/teacher')
   
#
#@route('/studentClassInfo/<classname>/<studentID>')
#def studentClassInfo(classname, studentID):
#    db = client.gradebook
#    classInfo = db.classes.find_one({"courseID": classname},{"teacher": 1, "courseTitle":1, "courseID":1})
#    #need to show assignment info for that class
#    #assignmentList = list(db.classes.find({"assignmentList" : {}}))
#    assignmentInfo = list(db.assignments.find({"assignmentID": {'$regex':classname},"studentID":studentID}, {"studentID": 1, "assignmentID": 1, "grade": 1}))
#
#    return template('show_assignments', classes = classInfo, assignment = assignmentInfo, classname = classname)

##this is a method to add assignments for a class that the teacher has clicked on
#@route('/<classname>/assignments')
#def teacherClassInfo(classname):
#    print(classname)
#    db = client.gradebook # database gradebook
#    classInfo = db.classes.find_one({"courseID": classname},{"teacher": 1, "courseTitle":1, "courseID":1})
#    #need to show assignment info for that class
#    #assignmentList = list(db.classes.find({"assignmentList" : {}}))
#    assignmentInfo = list(db.assignments.find({"assignmentID": {'$regex':classname},"studentID":username}, {"studentID": 1, "assignmentID": 1, "grade": 1}))
#
#    return template('show_assignments', classes = classInfo, assignments = assignmentInfo)

run(host='localhost', port=8080, debug=True)
