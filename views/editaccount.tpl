<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags always come first -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">

    <title>Xmas Store</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/css/bootstrap.min.css" integrity="sha384-AysaV+vQoT3kOAXZkl02PThvDr8HYKPZhNT5h/CXfBThSRXQ6jW5DO2ekP5ViFdi" crossorigin="anonymous">

    <link href="static/style.css" rel="stylesheet">

</head>
<body>

    <div class="container">

        <div class="row">

            <div class="col-xs-12">
                <h1 style="margin-bottom:30px;text-align:center;">Greetings!</h1>
                <h3>{{error}}</h3>
            </div>

            <!--
            On this page:
                > buttons for:
                    - EDIT ACCOUNT
                    - BACK TO MAIN PAGE
                    - SHOW ORDER HISTORY
                    - DELETE ACCOUNT


            <form method='get' action="/shoppermain?id={{sid}}">
                <button type="submit" class="btn btn-outline-primary btn-lg customBtn">Back</button>
            </form>
            -->

            <a href="/shoppermain?sid={{sid}}">Back</a>

            <table class="table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Address</th>
                        <th>Username</th>
                    </tr>
                </thead>
                <tbody>
                    % for i in details:
                    <tr>
                        <th scope="row">{{i[0]}}</th>
                        <th>{{i[1]}}</th>
                        <th>{{i[2]}}</th>
                        <th>{{i[3]}}</th>
                        <th>{{i[4]}}</th>
                    </tr>
                    % end
            </table>

            <form method="post">
                <div class="form-group">
                    <label for="editSelect">Select What to Edit:</label>
                    <select name="toEdit" id="editSelect">
                        <option value="firstname">First Name</option>
                        <option value="lastname">Last Name</option>
                        <option value="address">Address</option>
                        <option value="username">Username</option>
                    </select>
                </div>

                <div class="form-group">
                    <input type="text" name="newValue">
                </div>
                <input type="submit" name="submit" value="Submit">

                <input type="hidden" name="custId" value="{{sid}}">
            </form>


        </div>

    </div>

<!-- jQuery first, then Tether, then Bootstrap JS. -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha384-3ceskX3iaEnIogmQchP8opvBy3Mi7Ce34nWjpBIwVTHfGYWQS9jwHDVRnpKKHJg7" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.3.7/js/tether.min.js" integrity="sha384-XTs3FgkjiBgo8qjEjBk0tGmf3wPrWtA6coPfQDfFEY8AnYJwjalXCiosYRBIBZX8" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>
</body>
</html>
