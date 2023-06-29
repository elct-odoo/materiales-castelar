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
-------------------------------------------------------------------------------------------------------------------------------------------------------------
