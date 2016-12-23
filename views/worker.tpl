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
        <div class="main">
            <h1 style="margin-bottom:30px" >Worker Page</h1>
            <form method="get" action="/newitem">
                <button style="margin-bottom:30px;" type="submit" class="btn btn-outline-primary btn-lg">Add New Item</button>
                <button formaction="/" style="margin-bottom:30px;" type="submit" class="btn btn-outline-primary btn-lg">Back to Main Page</button>
            </form>

            <table class="table">
                <thead>
                    <tr>
                        <th>Item ID</th>
                        <th>Name</th>
                        <th>Purchase Price (£)</th>
                        <th>Sale Price (£)</th>
                        <th>Stock Level</th>
                        <th>Add New Stock (enter number of stock to be added)</th>
                    </tr>
                </thead>
                <tbody>
                    % for i in items:
                    <tr>
                        <th scope="row">{{i[0]}}</th>
                        <td>{{i[1]}}</td>
                        <td>{{i[2]}}</td>
                        <td>{{i[3]}}</td>
                        <td>{{i[4]}}</td>
                        <td>
                            <form method="post" action="/worker">
                                <input type="number" name="newStock.{{i[0]}}">
                                <input style="margin-left: 5px;" type="submit" Value="Submit">
                            </form>
                        </td>
                    </tr>
                    % end
                </tbody>
            </table>

        </div>
    </div>

    <!-- jQuery first, then Tether, then Bootstrap JS. -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha384-3ceskX3iaEnIogmQchP8opvBy3Mi7Ce34nWjpBIwVTHfGYWQS9jwHDVRnpKKHJg7" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.3.7/js/tether.min.js" integrity="sha384-XTs3FgkjiBgo8qjEjBk0tGmf3wPrWtA6coPfQDfFEY8AnYJwjalXCiosYRBIBZX8" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>
  </body>
</html>
