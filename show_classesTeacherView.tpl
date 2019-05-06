<!DOCTYPE html>
<link rel='stylesheet' type='text/css' href='/css/style.css'>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class</title>
</head>
<body>

<form action="/update" method="post">
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
    <p> <b>Average Grade</b> {{avgGrade}} </p>

    <button name="update" type="submit">Save Updates</button>


<!-- start of assignments -->
    <table>

        <tr>

          <th>Student ID</th>
          <th>Assignment</th>
		  <th>Grade</th>

        </tr>
        % for assignments in assignments:
        <tr>
            <td><input type="text" name="studentID" value="{{assignments['studentID']}}" readonly></td>
            <td><input type="text" name="assignmentID" value="{{assignments['assignmentID']}}" readonly></td>
            <td><input type=number name="grade" min="0" max="100"value="{{assignments['grade']}}"></td>
        </tr>
        % end

    </table>
</form>
</body>
</html>
