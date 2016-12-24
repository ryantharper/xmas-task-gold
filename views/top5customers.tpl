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
            <h1>Top 5 Products</h1>

            <form method="get" action="">
                <button formaction="/worker" style="margin-bottom:30px;" type="submit" class="btn btn-outline-primary btn-lg">Back to Worker Page
                </button>
            </form>

            <p style="color:red"><b>Red + Bold Means the Item needs to be reordered.</b></p>

            <table class="table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Profit Made</th>
                        <th>Total Spent</th>
                    </tr>
                </thead>
                <tbody>
                    % for n in top5custs:
                    <tr>
                        <td>{{n[2]+" "+n[3]}}</td>
                        <td>{{n[1]}}</td>
                        <td>{{n[4]}}</td>
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
