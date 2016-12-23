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
            <h1 style="margin-bottom:10px;">Add New Item</h1>

            <form method="get">
                <button type="submit" formaction="/worker" class="btn btn-outline-primary btn-lg customBtn">Go Back</button>
            </form>

            <form method="post" action="/newitem">
                <div class="form-group">
                    <label for="nameI">Name of Item:</label><input type="text" id="nameI" name="nameItem" class="form-control">
                </div>
                <div class="form-group">
                    <label for="priceI">Price of Item:</label><input type="number" step=0.01 id="priceI" name="costItem" class="form-control">
                </div>
                <div class="form-group">
                    <label for="stockI">Stock Level: </label><input type="number" id="stockI" name="stockItem" class="form-control">
                </div>
                <div class="form-group">
                    <label for="catI">Item Category:</label>
                    <select name="catItem">
                        <option value="xmas_decs">Christmas Decorations</option>
                        <option value="xmas_food">Christmas Food</option>
                        <option value="xmas_electricals">Christmas Electricals</option>
                    </select>
                    <!--<input type="text" id="catI" class="form-control" name="catItem">-->
                </div>
                <div class="form-group">
                    <input type="submit" value="Submit" name="newItem">
                </div>
            </form>
        </div>
    </div>

    <!-- jQuery first, then Tether, then Bootstrap JS. -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha384-3ceskX3iaEnIogmQchP8opvBy3Mi7Ce34nWjpBIwVTHfGYWQS9jwHDVRnpKKHJg7" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.3.7/js/tether.min.js" integrity="sha384-XTs3FgkjiBgo8qjEjBk0tGmf3wPrWtA6coPfQDfFEY8AnYJwjalXCiosYRBIBZX8" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>
  </body>
</html>
