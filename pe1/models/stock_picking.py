from odoo import api, fields, models
from odoo.exceptions import ValidationError

class StockPicking(models.Model):
    _inherit='stock.picking'

    quantity_demand = fields.Float(related="move_ids.product_uom_qty")
    quantity_done = fields.Float(related="move_ids.quantity_done")

    @api.constrains("quantity_demand", "quantity_done")
    def button_validate(self):
        for record in self:
            if record.quantity_done > record.quantity_demand:
                raise ValidationError("Quantity done cannot be greater than quantity demand.")
            else: 
                return super()
