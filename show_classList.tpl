<!DOCTYPE html>
<link rel='stylesheet' type='text/css' href='/static/style.css'>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Students Enrolled</title>
</head>
<body>

<form action="/createAssignment" method="post">
	<table>
        <tr>
            <th>Professor</th>
            <th>Course</th>
            <th>ID</th>
        </tr>
      <!--  % for classes in classes:-->
        <tr>
            <td>{{classes['teacher']}}</td>
            <td>{{classes['courseTitle']}}</td>
            <td><input type="text" name="classname" value="{{classes['courseID']}}" readonly></td>
        </tr>
    </table>
    <p> <b>Average Grade For Class : </b> {{avgGrade}} </p>
 <!-- this is to display assignments for specific class -->
<table>


  <th>Assignment</th>
  % for assignmentList in assignmentList:
	<br>
	% for assignment in assignmentList['assignmentList']:
	<tr><td><input type="text" name="assignmentID" value="{{assignment}}" readonly></td></tr>
% end


</table>
<center>
    <button name="addAssignment" type="submit">Add Assignment</button>
</center></form>
	<!-- start of students in class list -->
    <table>
<th>Students Currently Enrolled: </th>
        
		% for classList in classList:
			<br>
  			% for student in classList['classList']:
			<tr><td><a href="http://localhost:8080/teacherViewStudentAssignments/{{classname}}/{{student}}">{{student}}</a></td></tr>
        
		% end
       

    </table>


</body>
</html>
