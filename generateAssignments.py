from pymongo import MongoClient
import random

client = MongoClient('mongodb+srv://user:user123@cluster0-7i1kc.mongodb.net/test?retryWrites=true')
db = client.gradebook
students = db.students.find({},{"_id":0, "studentID":1})

print("All the current documents in our collection:")
for doc in students:
    print(doc)
    
def getGrade():
    grade = random.randrange(50,100)
    print(grade)
    return grade

i = 1
for assignments in range(30):
    ass =   "Chem201-01-F2018-" + str(i)
    #create the assignmentID and update to assignment collection
    myquery = { "courseID": "Chem201-01-F2018" }
    newvalues = { "$addToSet": { "assignmentList": ass } }
    db.classes.update_one(myquery, newvalues)
   
    grade = getGrade()
#    #insert an assignment document into assignment collection
    assignment= {"studentID": "ai7321lr", "assignmentID": ass, "grade":grade}
    try:
        db.assignments.insert_one(assignment)
    except Exception as e:
        print ("insert failed:", e)
    i+=1
    print(ass)
results = db.classes.find()
for entry in results:
    print(entry)




#### INSERT assignment DOCUMENT ##
#assignment= {"studentID": "in8738bw", "assignmentID": ass, "grade":grade} 
#
#try:
#    assignments.insert_one(doc)
#except Exception as e:
#    print ("insert failed:", e)
## print the songs to verify insertion
#results = assignments.find()
#for entry in results:
#    print(entry)