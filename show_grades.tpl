<!DOCTYPE html>
<link rel='stylesheet' type='text/css' href='/static/style.css'>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grades</title>
</head>
<body>

    <table>

        <tr>

            <th>Assignment</th>
            <th>Grade</th>
            <th>Overall Grade</th>



        </tr>
        % for assignments in assignments:
        <tr>
            <td>{{assignments['assignmentID']}}</td>
            <td>{{assignments['grade']}}</td>
            <td>{{totalgrade}}</td>
        </tr>
        % end

    </table>

</body>
</html>
