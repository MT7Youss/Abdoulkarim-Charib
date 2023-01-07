from odoo import fields, models, Command

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    ###########################
    #add filds 
    #Training Date
    #############################
    training_date = fields.Char(string="Training Date")
    notes = fields.Text(string='Notes', required=False)
