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
                <h1 style="margin-bottom:30px;text-align:center;">Greetings, {{shopperName}}!</h1>
            </div>

            <!--
            On this page:
                > buttons for:
                    - EDIT ACCOUNT
                    - BACK TO MAIN PAGE
                    - SHOW ORDER HISTORY
                    - DELETE ACCOUNT
            -->

            <form method='get' style="margin-bottom:20px; text-align:center">
                <button type="submit" formaction="/editaccount" class="btn btn-outline-primary btn-lg">Edit Account</button>
                <button type="submit" formaction="/" class="btn btn-outline-primary btn-lg">Home</button>
                <button type="submit" formaction="/orders" class="btn btn-outline-primary btn-lg">Order History</button>
                <button type="submit" formaction="/delete" class="btn btn-outline-primary btn-lg">Delete Account</button>
            </form>

            <div class="col-md-8">
                % for i in items:
                <div class="col-sm-6">
                    <div class="card card-block">
                        <p class="card-title"><b>{{i[1]}}</b></p>
                        <p class="card-text">£{{i[3]}}</p>
                        <form method="post" action="/shoppermain">
                            <label>Qty:</label>
                            <select name="numItems.{{i[0]}}">
                                % for n in range(i[4]):
                                <option value="{{n+1}}">{{n+1}}</option>
                                % end
                            </select>
                            <input type="submit" value="Add to Cart">
                        </form>
                    </div>
                </div>
                % end
            </div>

            <div class="col-md-3" style="margin-left:0px">
                <h3>Cart</h3>


                <table class="table table-striped table-bordered table-hover">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Qty</th>
                            <th>Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        % for a in basket:
                        <tr>
                            <td>{{a[1]}}</td>
                            <td>{{a[2]}}</td>
                            <td>£{{a[3]}}</td>
                            <td>
                            		<form method="post" action="/shoppermain">
																		<input type="hidden" name="orderItemId" value="{{a[0]}}">
																		<input type="submit" name="delItem" value="X">
                            		</form>
                            </td>
                        </tr>
                        %end
                    </tbody>
                    <tfoot>
                        <tr>
                            <th></th>
                            <th>Total Cost:</th>
                            <th></th>
                        </tr>
                    </tfoot>
                </table>

            </div>

        </div>
    </div>

<!-- jQuery first, then Tether, then Bootstrap JS. -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha384-3ceskX3iaEnIogmQchP8opvBy3Mi7Ce34nWjpBIwVTHfGYWQS9jwHDVRnpKKHJg7" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.3.7/js/tether.min.js" integrity="sha384-XTs3FgkjiBgo8qjEjBk0tGmf3wPrWtA6coPfQDfFEY8AnYJwjalXCiosYRBIBZX8" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>
</body>
</html>
