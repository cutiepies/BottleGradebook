<!DOCTYPE html>
<link rel='stylesheet' type='text/css' href='/css/style.css'>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Students Enrolled</title>
</head>
<body>


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
            <td>{{classes['courseID']}}</td>
        </tr>
    </table>
    <p> <b>Average Grade For Class : </b> {{avgGrade}} </p>
 <!-- this is to display assignments for specific class -->
<table>

<tr>
  <th>Assignment</th>
  % for assignmentList in assignmentList:
	<td>{{assignmentList['assignmentList']}}</td>

% end
</tr>

</table>
<center><form action="/createAssignment" method="post">
    <button name="addAssignment" type="submit">Add Assignment</button>
</form></center>
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
