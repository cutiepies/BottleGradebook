<!DOCTYPE html>
<link rel='stylesheet' type='text/css' href='/static/css/style.css'>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class</title>
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
    <p> <b>Average Grade</b> {{avgGrade}} </p>
<!-- start of assignments -->
    <table>

        <tr>

          <th>Student ID</th>
          <th>Assignment</th>
          <th>Grade</th>




        </tr>
        % for assignments in assignments:
        <tr>
            <td>{{assignments['studentID']}}</td>
            <td>{{assignments['assignmentID']}}</td>
            <td>{{assignments['grade']}}</td>
        </tr>
        % end

    </table>

</body>
</html>
