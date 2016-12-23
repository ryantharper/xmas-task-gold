"""
THIS RUNS A WEB SERVER WITH BOTTLE, WITH THE 'silverBOTTLE.py' FILE AS THE 'BACKEND'

BOTTLE --
SILVER TO DO:

>SHOPPER OPTS:
    - LOGIN
    - CREATE ACCOUNT
    - GO BACK [to worker/shopper page]

> LOGGING IN:
    - JUST REQUIRE USERNAME //// OR SELECT USER??

> WHEN LOGGED IN:
    - BUY ITEM
    - SEE ORDER HISTORY
    - EDIT ACCOUNT DETAILS
    - DELETE ACCOUNT
    - GO BACK [to worker/shopper page]

    ;> maybe DO shopper?id=XX  -> this used for order table

"""

# Bottle Imports
from bottle import route, run, static_file, template, request, redirect
# Gets Store class from main Python file.
from xmasTaskGold import Store
# other imports
import sqlite3 as lite
import sys

# Creates instance of the store class with the database and table names.
store = Store(lite.connect('festiveshop.db'))



# Main Index Page
@route('/')
def index():
    return template("index")

# for CSS
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')

# shopper splash page -- choose login, create acc or go back

@route('/shopper')
def mainShopper():
    return template('shopper')

# when post -> redirect to login page OR go back to newaccount if username taken

@route('/newaccount', method='GET')
def newAccount():
    try:
        pageError = request.query.error
    except:
        pageError = "Hello, Shopper!"
    return template('newaccount', error=pageError)

@route('/newaccount', method='POST')
def createAccount():
    store.c.execute("SELECT username FROM customers")
    validUsernames = [u[0] for u in store.c.fetchall()]

    firstname = request.forms.get('firstname')
    lastname = request.forms.get('lastname')
    address = request.forms.get('address')
    username = request.forms.get('username')

    if username not in validUsernames: # username GOOD -- go to login page & create acc
        store.insert_data_cust(firstname, lastname, address, username)
        return redirect('login')
    else: # username BAD -- go to taken page
        return redirect('newaccount?error=Username Taken')



@route('/login', method='GET')
def loginPage():
    try:
        pageError = request.query.error
    except:
        pageError = "Hello, Shopper!"

    return template('login', error=pageError)


@route('/login', method='POST')
def loginPagePost():
    store.c.execute("SELECT username FROM customers")
    validUsernames = [u[0] for u in store.c.fetchall()]

    username = request.forms.get('username')
    if username in validUsernames:
        store.c.execute("SELECT id FROM customers WHERE username='{}'".format(username))
        sid = store.c.fetchone()[0]
        return redirect('/shoppermain?sid={}'.format(sid))
    else:
        return redirect('login?error=Wrong Username')
    #return template('login')

### SHOPPER PAGE ###

@route('/shoppermain', method='GET')
def shopperPage():
    global userId
    userId = request.query.sid
    store.c.execute("SELECT firstname FROM customers WHERE id=?", (userId,))
    name = store.c.fetchone()[0]
    return template('shoppermain', items=store.printItems(1), shopperName=name)

# DOES STUFF WITH FORM -> when shopper buys item
@route('/shoppermain', method='POST')
def shopperPage2():
    for k in request.forms:
        if k.startswith('numItems.'):
            itemId = k.partition('.')[-1]
            numItems = int(request.forms.get(k))
            store.updateStock(itemId,-numItems)
            store.insert_data_order(userId,itemId,numItems)

    return redirect('/shoppermain?sid={}'.format(userId)) # redirects to shoppermain func

# EDIT ACCOUNT
@route('/editaccount', method='GET')
def editAccountPage():
    try:
        pageError = request.query.error
    except:
        pageError = "Hello, Shopper!"

    store.c.execute("SELECT * FROM customers WHERE ID={}".format(userId))
    userDetails = store.c.fetchall()

    return template('editaccount', details=userDetails, sid=userId, error=pageError)

@route('/editaccount', method='POST')
def editAccountPagePost():
    store.c.execute("SELECT username FROM customers")
    validUsernames = [u[0] for u in store.c.fetchall()]

    custId = request.forms.get('custId')
    colToEdit = request.forms.get('toEdit')
    newValue = request.forms.get('newValue')

    if colToEdit =='username' and newValue in validUsernames: # bad --> username taken
        return redirect('/editaccount?error=Username Taken')
    else:
        store.updateUserAcc(custId, colToEdit, newValue)
        return redirect('/editaccount')


# ORDER HISTORY
@route('/orders')
def orderHistory():
    orderDetails = store.showOrderHistory(userId)
    return template('orders', details = orderDetails, sid=userId)

# DELETE ACCOUNT
@route('/delete', method='GET')
def deleteAccount():
    return template('delete', sid=userId)

@route('/delete', method='POST')
def delete():
    store.deleteUser(userId)
    redirect('/shopper')

### WORKER PAGE ###

@route('/worker', method='GET')
def workerPage1():
    return template('worker', items=store.printItems(2))

# Gets ITEMID of the item whose stock is being changed.
@route('/worker', method='POST')
def workerPage2():
    for k in request.forms:
        if k.startswith('newStock.'):
            itemId = k.partition('.')[-1]
            numStock = request.forms.get(k)
            store.updateStock(itemId,numStock)

    return redirect('worker')

### ADD NEW ITEM PAGE ###
@route('/newitem', method='GET')
def newItemPage1():
    return template('newitem')

# DOES STUFF WITH ADD ITEM FORM --> adds item
@route('/newitem', method='POST')
def newItemPage2():
    nameItem = request.forms.get('nameItem')
    costItem = request.forms.get('costItem')
    stockItem = request.forms.get('stockItem')
    catItem = request.forms.get('catItem')
    store.addItemWeb(nameItem, costItem, stockItem, catItem)
    return template('newitem')




run(host='localhost', port='8080', debug=True)
