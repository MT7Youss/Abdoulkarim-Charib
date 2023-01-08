from odoo import api, models, _, fields
from odoo.exceptions import ValidationError
from erppeek import Client
########################################################################
##utilisteur pas defaut 
############################################################
odoo = Client("http://odoo.example.com", db="mydatabase", user="user", password="password")

###############################################################################
##logique de vente d'une formation qui cree des events de calendrier 
##########################################################################
calendar = odoo.model("calendar.event")

order = sale_order.create({
    "partner_id": 1,
    "order_line": [
        (0, 0, {
            "product_id": product_id,
            "price_unit": price_unit,
        })
    ]
})

calendar = odoo.model("calendar.event")
task = calendar.create({
    "name": activity_calendar_event_id,
    "start": "",
    "stop": "2022-01-01 01:00:00",
    "allday": False,
    "state": "open",
    "user_id": partner_id.company_id.name,
})




class SaleOrder(models.Model):
    _inherit = 'sale.order'
