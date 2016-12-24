"""
Ryan Harper

Christmas Task : GOLD

Extra Python Packages Used:
    - Bottle [web server]


------------------------------------------------------------------
'Did you hear about the movie they made about the database admin?'

'There was NoSQL.'
------------------------------------------------------------------


things to do/work out
    - report
    - reward
    - tell user if top 5



"""

import sqlite3 as lite, os, sys
#from tabulate import tabulate
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
        lastname TEXT NOT NULL, address TEXT NOT NULL, username TEXT NOT NULL, orders INTEGER NOT NULL, top5 BOOLEAN)""")

    # for first run -- ORDERS
    def createTableOrders(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, custId INTEGER,
        itemId INTEGER, quantity INTEGER NOT NULL, cost REAL NOT NULL, profit REAL NOT NULL, FOREIGN KEY(itemId) REFERENCES items(id), FOREIGN KEY(custId) REFERENCES customers(id))""")

    # --------------------- TABLE FOR CURRENT ORDER ---------------------

    def createTableCurrentOrders(self): # create on login
        self.conn.execute("DROP TABLE IF EXISTS current_order")
        self.conn.execute("""CREATE TABLE current_order (id INTEGER PRIMARY KEY, itemId INTEGER, quantity INTEGER, cost REAL, FOREIGN KEY(itemId) REFERENCES items(id))""")

    def insert_data_current_order(self, itemId, qty):
        self.c.execute("SELECT saleCost FROM items WHERE id={}".format(itemId))
        cost = self.c.fetchall()[0][0]
        cost = qty * float(cost)
        self.conn.execute("INSERT INTO current_order (itemId, quantity, cost) VALUES (?, ?, ?)", (itemId, qty, cost))
        self.conn.commit()

    def getItemDetails_CurrentOrder(self):
        self.c.execute("SELECT id, itemId, quantity, round(cost, 2) FROM current_order") #[0]=id, [1]=itemId, [2]=qty, [3]=cost
        currentOrdersTuples = self.c.fetchall()
        # creates list of lists instead of list of tuples --> becomes mutable
        currentOrders = [list(e) for e in currentOrdersTuples]

        # replaces itemId with item name
        for n in currentOrders:
            self.c.execute("SELECT name FROM items WHERE id={}".format(n[1]))
            n.append(n[1]) # used for when buying -- adds item ID to list
            n[1] = self.c.fetchall()[0][0]


        return currentOrders

    def removeOrder(self, id_):
        self.conn.execute("DELETE FROM current_order WHERE id={}".format(id_))
        self.conn.commit()

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
    def insert_data_order(self, custId, itemId, qty):
        self.c.execute("SELECT saleCost FROM items WHERE id={}".format(itemId))
        costTotal = self.c.fetchone()[0]
        self.c.execute("SELECT purchCost FROM items WHERE id={}".format(itemId))
        purchCost = self.c.fetchone()[0]
        cost = int(qty) * costTotal
        profit = cost-(int(qty)*purchCost)
        self.conn.execute("INSERT INTO orders (custId, itemId, quantity, cost, profit) VALUES (?, ?, ?, ?, ?)", (custId, itemId, qty, cost, profit))
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
            self.c.execute("SELECT id, name, round(purchCost, 2), round(saleCost, 2), stock_lvl, cat, quantity_bought FROM items WHERE stock_lvl > 0") # gets item where the stock is not zero
            return self.c.fetchall()
        else: # for workers
            self.c.execute("SELECT id, name, round(purchCost, 2), round(saleCost, 2), stock_lvl, cat, quantity_bought FROM items") # gets all items
            return self.c.fetchall()

    def updateUserAcc(self, custId, col, new):
        self.conn.execute("UPDATE customers SET {0} = '{1}' WHERE id={2}".format(col, new, custId))
        self.conn.commit()

    # TOP 5

    # TOP 5 PRODUCTS

    def top5products(self):
        self.c.execute("SELECT name, quantity_bought, stock_lvl FROM items")
        itemList = self.c.fetchall()
        itemListT5 = sorted(itemList, key=lambda t: t[1], reverse=True)[:5] # sorts list of tuples by qty bought, then splices so its only top 5

        return itemListT5

    def top5custs(self):
        self.c.execute("SELECT id, firstname, lastname FROM customers")
        custIdList = self.c.fetchall() # [(id, fn, ln)] -- gets customer info and id

        profitList = []
        # collects profit made by customer and amount spent by customer
        for i in custIdList:
            self.c.execute("SELECT profit FROM orders WHERE custId={}".format(i[0]))
            profits = self.c.fetchall()

            self.c.execute("SELECT cost FROM orders WHERE custId={}".format(i[0]))
            costs = self.c.fetchall()

            profitList.append((i[0], float("%.2f"%sum([p[0] for p in profits])), i[1], i[2], float("%.2f"%sum([c[0] for c in costs]))))

        # [(UserId, Profit, Fname, Lname, Costs)]
        #print(profitList)

        custListT5 = sorted(profitList, key=lambda t: t[1], reverse=True)[:5] # sorts list of tuples by PROFIT, then splices so its only top 5

        for i in custListT5:
            self.conn.execute("UPDATE customers SET top5 = 1 WHERE id={}".format(i[0]))
            self.conn.commit()

        return custListT5




# USED IN CMD/IDLE
def main():
    dbFilename = 'festiveshop.db'
    dbNew = not os.path.exists(dbFilename)
    store = Store(lite.connect(dbFilename))

    if dbNew:
        store.initDb()
    else:
        print("Database exists, assuming table and initial items do too.")

    #store.insert_data_order(4)

    #store.top5products()

    #store.top5custs()


main()
