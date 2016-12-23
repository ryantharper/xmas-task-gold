"""
Ryan Harper

Christmas Task : GOLD

Extra Python Packages Used:
    - Bottle [web server]


-> 'qtyBought' column in ITEMS table to increment by quantity bought by customer
-> 'orders' column in CUSTOMERS table to increment by 1 every time user presses buy // items bought if cant do multiple items in order table
-> on web -> instead of "buy", "add to basket" --> basket shows on side, option to buy at bottom -> basket updates everytime user clicks add to basket

things to do/work out

    multiple items in order table?



"""

import sqlite3 as lite, os, sys
from tabulate import tabulate
# BASE ITEMS, WILL BE ENTERED ON FIRST RUN
items = [{'name': 'Baubles 50 pk', 'purchCost': 3.00, 'saleCost': 5.00, 'stock_lvl': 30,'cat':'xmas_decs', 'qtyBought':3},
            {'name': 'Tinsel Red', 'purchCost':0.50, 'saleCost': 1.00, 'stock_lvl': 25,'cat':'xmas_decs', 'qtyBought':1},
            {'name': 'Tinsel Gold', 'purchCost': 0.50, 'saleCost': 1.00, 'stock_lvl': 35,'cat':'xmas_decs', 'qtyBought':2},
            {'name': 'Christmas Tree', 'purchCost': 59.99, 'saleCost': 80.00, 'stock_lvl': 20,'cat':'xmas_decs', 'qtyBought':0},
            {'name': 'Tree Lights', 'purchCost': 3.00, 'saleCost': 7.00, 'stock_lvl': 30,'cat':'xmas_decs', 'qtyBought':0},
            {'name': 'Tree Star', 'purchCost': 1.00, 'saleCost': 2.00, 'stock_lvl': 25,'cat':'xmas_decs', 'qtyBought':0},
            {'name': 'Turkey', 'purchCost': 9.99, 'saleCost': 20.00, 'stock_lvl': 20,'cat':'xmas_food', 'qtyBought':0},
            {'name': 'Potatoes 2kg', 'purchCost': 0.80, 'saleCost': 1.50, 'stock_lvl': 35,'cat':'xmas_food', 'qtyBought':0},
            {'name': 'Carrots 1kg', 'purchCost': 0.60, 'saleCost': 1.00, 'stock_lvl': 25,'cat':'xmas_food', 'qtyBought':0},
            {'name': 'Parsnips 1kg', 'purchCost': 0.80, 'saleCost': 1.80, 'stock_lvl': 15,'cat':'xmas_food', 'qtyBought':0},
            {'name': 'Pigs in Blankets 20pk', 'purchCost': 1.20, 'saleCost': 2.00, 'stock_lvl': 40,'cat':'xmas_food', 'qtyBought':0},
            {'name': 'Stuffing 200g', 'purchCost': 0.90, 'saleCost': 1.50, 'stock_lvl': 29,'cat':'xmas_food', 'qtyBought':0},
            {'name': 'Celebrations Box', 'purchCost': 1.50, 'saleCost': 3.00, 'stock_lvl': 18,'cat':'xmas_food', 'qtyBought':0},
            {'name': 'Prosecco 75cl', 'purchCost': 4.99, 'saleCost': 6.50, 'stock_lvl': 13,'cat':'xmas_food', 'qtyBought':0},
            {'name': 'Mixed Nuts 500g', 'purchCost': 1.20, 'saleCost': 3.00, 'stock_lvl': 27,'cat':'xmas_food', 'qtyBought':0},
            {'name': 'iPad Air 2', 'purchCost': 399.99, 'saleCost': 499.99, 'stock_lvl': 18,'cat':'xmas_electricals', 'qtyBought':0},
            {'name': 'Fitbit', 'purchCost':49.99, 'saleCost':75.00, 'stock_lvl': 23,'cat':'xmas_electricals', 'qtyBought':0},
            {'name': 'Xbox One S', 'purchCost': 199.99, 'saleCost': 250.00, 'stock_lvl': 32,'cat':'xmas_electricals', 'qtyBought':0},
            {'name': 'Kindle Paperwhite', 'purchCost': 74.99, 'saleCost': 104.49, 'stock_lvl': 22,'cat':'xmas_electricals', 'qtyBought':0},
            {'name': 'Parrot Drone', 'purchCost': 410.00, 'saleCost': 499.99, 'stock_lvl': 11,'cat':'xmas_electricals', 'qtyBought':0},
            {'name': 'Smart Kettle', 'purchCost': 59.99, 'saleCost': 74.50, 'stock_lvl': 24,'cat':'xmas_electricals', 'qtyBought':0},
            {'name': 'Oral-B Electric Toothbrush', 'purchCost':69.99, 'saleCost': 94.99, 'stock_lvl': 13,'cat':'xmas_electricals', 'qtyBought':0}]

# BASE CUSTOMER LIST
customers = [{'firstname':'Ryan', 'lastname':'Harper', 'address':'123 Example Road', 'username':'rtharper', 'orders':2},
            {'firstname':'John', 'lastname':'Smith', 'address':'456 Road Avenue', 'username':'jsmith', 'orders':1},
            {'firstname':'Lucy', 'lastname':'Jones', 'address':'321 Mini Street', 'username':'ljones', 'orders':0},
            {'firstname':'Luke', 'lastname':'Hayward', 'address':'45 Withers Close', 'username':'lukehay', 'orders':0},
            {'firstname':'Jade', 'lastname':'Robson', 'address':'63 Sutton Lane', 'username':'jaderobson', 'orders':0},
            {'firstname':'Zara', 'lastname':'Evans', 'address':'55 Wheel Road', 'username':'zevans', 'orders':0},
            {'firstname':'Jack', 'lastname':'Mason', 'address':'46 Dover Road', 'username':'jamason', 'orders':0}]

# BASE ORDER LIST
orders = [
            {'custId':1, 'itemId':2,  'quantity':1, 'groupId':1},
            {'custId':1, 'itemId':3, 'quantity':2, 'groupId':1},
            {'custId':2, 'itemId':1, 'quantity':3, 'groupId':2}
        ]

workerPass = "pass123word"

# Store Class
class Store:
    # initialise object
    def __init__(self, conn):
        self.conn = conn # db connection
        self.c = self.conn.cursor() # create cursor to get output

    # if first run of program & no db; creates table & inserts data if it doesn't exist
    def initDb(self):
        self.createTableItems()
        self.createTableCustomers()
        self.createTableOrders()

        for i in items:
            self.insert_data_stock(i['name'], i['purchCost'], i['saleCost'], i['stock_lvl'], i['cat'], i['qtyBought'])

        for i in customers:
            self.insert_data_cust(i['firstname'], i['lastname'], i['address'], i['username'], i['orders'])

        for i in orders:
            self.insert_data_order(i['custId'], i['itemId'], i['quantity'])

        self.conn.commit()

    # --------------------- CREATE TABLES ---------------------

    # for first run -- ITEMS
    def createTableItems(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT NOT NULL,
        purchCost REAL NOT NULL, saleCost REAL NOT NULL, stock_lvl INTEGER NOT NULL, cat TEXT NOT NULL, quantity_bought INTEGER NOT NULL)""")

    # for first run -- CUSTOMERS
    def createTableCustomers(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, firstname TEXT NOT NULL,
        lastname TEXT NOT NULL, address TEXT NOT NULL, username TEXT NOT NULL, orders INTEGER NOT NULL)""")

    # for first run -- ORDERS
    def createTableOrders(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, custId INTEGER,
        itemId INTEGER, quantity INTEGER NOT NULL, cost REAL NOT NULL, FOREIGN KEY(itemId) REFERENCES items(id), FOREIGN KEY(custId) REFERENCES customers(id))""")

    # --------------------- INSERTS ---------------------

    # ADD NEW -- ITEM
    def insert_data_stock(self, name, purchCost, saleCost, stock_lvl, cat, qtyBought=0):
        self.conn.execute("INSERT INTO items (name, purchCost, saleCost, stock_lvl, cat, quantity_bought) VALUES (?, ?, ?, ?, ?, ?)", (name, purchCost, saleCost, stock_lvl, cat, qtyBought))
        self.conn.commit()

    # ADD NEW -- CUSTOMER
    def insert_data_cust(self,fname,lname,addr,usrname,orders=0):
        self.conn.execute("INSERT INTO customers (firstname, lastname, address, username, orders) VALUES (?, ?, ?, ?, ?)", (fname, lname, addr, usrname, orders))
        self.conn.commit()

    # ADD NEW -- ORDER
    def insert_data_order(self,custId,itemId,qty):
        self.c.execute("SELECT saleCost FROM items WHERE id={}".format(itemId))
        costTotal = self.c.fetchall()[0][0]
        cost = int(qty) * costTotal
        self.conn.execute("INSERT INTO orders (custId, itemId, quantity, cost) VALUES (?, ?, ?, ?)", (custId, itemId, qty, cost))
        self.conn.commit()

    # --------------------- others ---------------------

    def deleteUser(self, custId):
        self.conn.execute("DELETE FROM customers WHERE id={}".format(custId))
        self.conn.execute("DELETE FROM orders WHERE custId={}".format(custId))
        self.conn.commit()

    def addItemWeb(self, name, purchCost, saleCost, stock_lvl, cat):
        self.insert_data_stock(name, purchCost, saleCost, stock_lvl, cat)
        self.conn.commit()


    def updateStock(self, idn, change):
        self.c.execute("SELECT stock_lvl FROM items WHERE id={}".format(idn)) # gets stock_lvl of the item corresponding to id
        currentStock = self.c.fetchall()[0][0] # gets stock_lvl
        newStock = currentStock + int(change) # alters stock level
        self.conn.execute("UPDATE items SET stock_lvl = {0} WHERE ID={1}".format(newStock, idn)) # updates stock level to new stock level
        self.conn.commit() # commits changes to table

    # SHOW ORDER HISTORY FOR USER

    def showOrderHistory(self,custId):
        self.c.execute("SELECT * FROM orders WHERE custId={}".format(custId))
        ordersTuples = self.c.fetchall()

        self.c.execute("SELECT name FROM items WHERE id=1")
        name = self.c.fetchall()[0][0]

        orders = [list(el) for el in ordersTuples]

        for i in orders:
            self.c.execute("SELECT name FROM items WHERE id={}".format(i[2]))
            i[2] = self.c.fetchall()[0][0]

        return orders


    def printItems(self, usr):
        if usr == 1: # for shoppers
            self.c.execute("SELECT * FROM items WHERE stock_lvl > 0") # gets item where the stock is not zero
            return self.c.fetchall()
        else: # for workers
            self.c.execute("SELECT * FROM items") # gets all items
            return self.c.fetchall()

    def updateUserAcc(self, custId, col, new):
        self.conn.execute("UPDATE customers SET {0} = '{1}' WHERE id={2}".format(col, new, custId))
        self.conn.commit()


# USED IN CMD/IDLE
def main():
    dbFilename = 'festiveshop.db'
    dbNew = not os.path.exists(dbFilename)
    store = Store(lite.connect(dbFilename))

    if dbNew:
        store.initDb()
    else:
        print("Database exists, assuming table and initial items do too.")

    #print(store.showOrderHistory(1))

    #loginUser(store)
    #store.showOrderHistory(1)
    #userOption(store)

main()
