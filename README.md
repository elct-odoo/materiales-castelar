# Materiales-Castelar

What is the business use case for this development?

Materiales Castelar wants to control receipts to make sure the different warehouses won't receive more than the ordered quantity.


Specification :

In Inventory app, in Receipts, when receiving the product, quantity_done must be equal or less than the demand (product_uom_qty). If the user enters a bigger quantity than the demand, a warning should appear saying "You can't receive more than the ordered quantity. Please, enter another quantity". 

This requirement is only for receipts and should work in all the different warehouses. 

Workflow:

1. Create a Purchase Order.

2. In Inventory, Receipts, enter a bigger quantity than the demand.

3. Warning should appear and the user must enter the correct quantity (equal or smaller than demand)

4. This will be tested in all the different warehouses
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Steps I took:

1.) Panic

2.) Created a new db -> personal1

3.) set password and login for db

3.) created a module under the inventory category named Quantity Manager

4.) Now since I have a base to work from I will try to understand the task by going through the work flow

5.) This step I am going to install the applications that I think will be necessary for this task in my fresh database

Apps: Inventory, Purchase
Dependencies: "stock", "purchase"

6.) First I need to get a better understanding of what a purchase order actually is.

7.) What currently happens when you enter a quantity larger than the demand? This is what we need to alter.

8.) After doing some testing it looks like after your create a purchase order it creates a receipt throuhg the inventory application

9.) Step 7 -> Lets test this:

Currently when you validate after making the 'Done' quantity larger than the demand it successfully validates. 

10.) Validate Button -> Where is this?

Button Validate is in Stock.Picking (Transfers) Makes sense since stock.picking is the main object for Internal moves

Let's try to overwrite this button in the model.

Next step is to find this button validate in the source code: 
odoo/addons/stock/models
/stock_picking.py

