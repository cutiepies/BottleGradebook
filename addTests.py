from pymongo import MongoClient
import random

client = MongoClient('mongodb+srv://user:user123@cluster0-7i1kc.mongodb.net/test?retryWrites=true')
db = client.gradebook
students = db.students.find({},{"_id":0, "studentID":1})



i = 1
for assignments in range(2):
    ass =   "Chem201-01-F2018-" + str(i)
    #myquery = { "assignmentID": ass, "studentID": "in8783bw"}
   
    #newvalues = { "$set" : {"type": "paper"} }
    #print(newvalues)
    db.assignments.update_one({ "assignmentID": ass, "studentID": "in8783bw"}, { "$set" : {"type": "paper"} })

 
    i+=1
    print(ass)
    assignmenttype = list(db.assignments.find({"assignmentID": ass, "studentID":"in8738bw"},{"assignmentID":1, "type":1}))
    print(assignmenttype)
    