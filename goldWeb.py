"""

- Prevent SQL injection

"""
# Bottle Imports
from bottle import app, route, run, static_file, template, request, redirect, app
# Gets Store class from main Python file.
from xmasTaskGold import Store
# other imports
import sqlite3 as lite, sys, ast

# Beaker
from beaker.middleware import SessionMiddleware

# Creates instance of the store class with the database and table names.
store = Store(lite.connect('festiveshop.db'))

sessions_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 300,
    'session.auto': True
}

bApp = SessionMiddleware(app(), sessions_opts)

#top5c = store.top5custs()

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

    # session
    s = request.environ.get('beaker.session')

    username = request.forms.get('username')
    if username in validUsernames:
        store.c.execute("SELECT id FROM customers WHERE username='{}'".format(username))
        shopperid = store.c.fetchone()[0] # (was sid=..)
        store.createTableCurrentOrders()

        s['sid'] = shopperid

        return redirect('/shoppermain')
        #return redirect('/shoppermain?sid={}'.format(sid))
    else:
        return redirect('login?error=Wrong Username')
    #return template('login')

### SHOPPER PAGE ###

@route('/shoppermain', method='GET')
def shopperPage():
    #global userId
    #userId = request.query.sid

    s = request.environ.get('beaker.session')
    userId = s['sid']
    #return str(userId)

    store.c.execute("SELECT firstname FROM customers WHERE id=?", (userId,))
    name = store.c.fetchone()[0]

    return template('shoppermain', items=store.printItems(1), shopperName=name, basket=store.getItemDetails_CurrentOrder())

# POST -> 'add to cart' and 'X' buttons, adds and removes to/from cart

@route('/shoppermain', method='POST')
def shopperPage2():

    s = request.environ.get('beaker.session')
    userId = s['sid']

    for k in request.forms:
        # ADDING ITEM TO BASKET
        if k.startswith('numItems.'):
            itemId = k.partition('.')[-1]
            numItems = int(request.forms.get(k))
            store.insert_data_current_order(itemId, numItems)
        # REMOVING ITEM FROM BASKET
        elif k =='orderItemId':
            ordItemId = request.forms.get(k)
            store.removeOrder(ordItemId)
        elif k == 'buyBasket':
            basket = ast.literal_eval(request.forms.get(k)) # itemid = basket[4]
            for order in basket:
                store.updateStock(order[4], -order[2])
                store.insert_data_order(userId,order[4],order[2])
                store.createTableCurrentOrders()
                # +1 in orders
                store.conn.execute("UPDATE customers SET orders = orders + {0} WHERE id={1}".format(order[2], userId))
                store.conn.execute("UPDATE items SET quantity_bought = quantity_bought + {0} WHERE id={1}".format(order[2], order[4]))
                store.conn.commit()
                print(order, file=sys.stderr)



    """
    for k in request.forms:
        if k.startswith('numItems.'):
            itemId = k.partition('.')[-1]
            numItems = int(request.forms.get(k))
            store.updateStock(itemId,-numItems)
            store.insert_data_order(userId,itemId,numItems)

    """
    return redirect('/shoppermain')
    #return redirect('/shoppermain?sid={}'.format(userId)) # redirects to shoppermain func

# EDIT ACCOUNT
@route('/editaccount', method='GET')
def editAccountPage():

    try:
        pageError = request.query.error
    except:
        pageError = "Hello, Shopper!"

    s = request.environ.get('beaker.session')
    userId = s['sid']

    store.c.execute("SELECT * FROM customers WHERE ID={}".format(userId))
    userDetails = store.c.fetchall()


    return template('editaccount', details=userDetails, error=pageError)
    #return template('editaccount', details=userDetails, sid=userId, error=pageError)

@route('/editaccount', method='POST')
def editAccountPagePost():
    store.c.execute("SELECT username FROM customers")
    validUsernames = [u[0] for u in store.c.fetchall()]

    s = request.environ.get('beaker.session')
    custId = s['sid']

    #custId = request.forms.get('custId')
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
    s = request.environ.get('beaker.session')
    userId = s['sid']
    orderDetails = store.showOrderHistory(userId)
    return template('orders', details = orderDetails)
    #return template('orders', details = orderDetails, sid=userId)

# DELETE ACCOUNT
@route('/delete', method='GET')
def deleteAccount():
    s = request.environ.get('beaker.session')
    userId = s['sid']
    return template('delete')
    #return template('delete', sid=userId)

@route('/delete', method='POST')
def delete():
    s = request.environ.get('beaker.session')
    userId = s['sid']
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

#################################################################
# TOP 5

# TOP 5 ITEMS
@route('/t5items')
def top5Items():
    top5i = store.top5products()
    #print(top5i, file=sys.stderr)
    return template('top5items', top5items = top5i)


@route('/t5customers')
def top5Customers():
    return template('top5customers', top5custs=top5c)

run(app=bApp, host='192.168.0.17', port=8080)
#run(host='localhost', port='8080', debug=True)
