<!DOCTYPE html>
<link rel='stylesheet' type='text/css' href='/static/css/style.css'>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignments</title>
</head>
<body>

    <table>

        <tr>
            <th>Student ID</th>
            <th>Assignment</th>
            <th>Grade</th>
            <th>Grade for Course</th>



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
