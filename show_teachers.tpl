<!DOCTYPE html>
<link rel='stylesheet' type='text/css' href='/static/css/style.css'>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teacher </title>
</head>
<body>

    <table>

        <tr>
            <th>Teacher ID: </th>
            <th>Email</th>
            <th>Name</th>

        </tr>
        % for teachers in teachers:
        <tr>
            <td>{{teachers['teacherID']}}</td>
            <td>{{teachers['email']}}</td>

            <td>{{teachers['name']}}</td>

            % for cl in teachers['classes']:
            <td><a href="http://localhost:8080/classList/{{cl}}">{{cl}}</a></td>
            % end
        </tr>
        % end

    </table>

</body>
</html>
