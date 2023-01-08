from odoo import fields, models, Command

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    ###########################
    #add filds 
    #Training Date
    #############################
    employee = fields.Char(string="employee")
    training_date = fields.Char(string="Training Date")
