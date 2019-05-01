<!DOCTYPE html>
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

        <tr>
          <th>Student ID</th>

       % for classList in classList:

           <td>{{classList['classList']}}</td>

       % end
       </tr>

    </table>


</body>
</html>
