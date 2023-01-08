from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    max_allowed_amount = fields.Float('Montant maximal autorisé')