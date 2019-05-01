<!DOCTYPE html>
<link rel='stylesheet' type='text/css' href='/static/style.css'>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Students Enrolled</title>
</head>
<body>

    <table>

        <tr>
            <th>Student ID: </th>
            <th>Email</th>

            <th>Name</th>
            <th>DOB</th>
            <th>Year</th>
            <th>Major</th>
            <th>Courses</th>


        </tr>
        % for students in students:
        <tr>
            <td>{{students['studentID']}}</td>
          <td>{{students['email']}}</td>

            <td>{{students['name']}}</td>
            <td>{{students['dob']}}</td>
            <td>{{students['year']}}</td>
            <td>{{students['major']}}</td>
            % for cl in students['classes']:
            <td><a href="http://localhost:8080/studentClassInfo/{{cl}}">{{cl}}</a></td>
            % end
        </tr>
        % end

    </table>

</body>
</html>
