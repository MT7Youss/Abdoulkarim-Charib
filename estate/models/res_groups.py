from odoo import fields, models

class ResGroups(models.Model):
    _inherit = 'res.groups'
    name = fields.Char(string='groupeDeGestionnaire')

