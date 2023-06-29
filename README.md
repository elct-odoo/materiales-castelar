# Materiales-Castelar
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





source control: 

created a local pe1 branch and set a remote upstream to origin pe1 will push remote changes to origin pe1 upon milestones

main will be saved for pull request at EOD

**
the only thing I am pushing directly to main is this read me
**
