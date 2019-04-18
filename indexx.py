
from bottle import route, run, HTTPResponse, template
from pymongo import MongoClient
import json

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
    username = request.forms.get('email')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
    
@route('/students')
def getstudents():

    db = client.gradebook
    students = list(db.students.find({}, {'_id': 0}))

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

        return json.dumps(asn)
    else: 
        raise HTTPResponse(status=204)

run(host='localhost', port=8080, debug=True)