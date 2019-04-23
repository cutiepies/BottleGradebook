
from bottle import route, run, HTTPResponse, template
from pymongo import MongoClient
import json
from bottle.ext.mongo import MongoPlugin

from bson.json_util import dumps

client = MongoClient('mongodb+srv://user:user123@cluster0-7i1kc.mongodb.net/test?retryWrites=true')
@route('/login') # or @route('/login')
def login():
    return 'Welcome to Gradebook. Please login with email to proceed!''''
    <form action="/login" method="post">
            Email: <input name="email" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
        '''
@route('/login', method='POST') #@post('/login') # or 
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
    
    
    
@route('/students')
def getstudents():

    db = client.gradebook
    students = list(db.students.find({}, {'studentID': "ak7221os"}))

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
    grades = list(db.assignments.find())
    return template('show_assignments', assignments = grades)


@route('/testClassInfo')
def testClassInfo():
    #pull classes from whoever logged in, and then display the class info for those classes
    #find how to join two collections
    #or use for loop to find.
 db = client.gradebook # database gradebook

    
#    classes = list(db.teacher.find({"teacherID": "mm1234"},{"teacherID": 1, "name":1, "classes":1}))
#    classInfo = list(db.classes.find({"classes": classes},{"teacher": 1, "courseTitle":1, "courseID":1}))
#    print(classes)
#    print(classInfo)



@route('/teacher')
def testtest():
    db = client.gradebook # database gradebook
    classes = list(db.teacher.find({"teacherID": "mm1234"},{"teacherID": 1, "name":1, "classes":1}))
    print(classes)

    #return template('show_assignments', assignments = grades)


run(host='localhost', port=8080, debug=True)