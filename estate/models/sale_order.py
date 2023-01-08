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
    
    # Ajoutez un champ de date de formation
    training_date = fields.Date('Date de formation')

    # Ajoutez un champ d'employé
    employee_id = fields.Many2one('hr.employee', string='Employé')
    
    #Montant
    amount = fields.Float('Montant dapprobation')

    @api.multi
    def action_confirm(self):
        # Récupérez les informations de la commande de vente
        training_date = self.training_date
        employee = self.employee_id

        # Créez un événement dans le calendrier de l'employé
        Event = self.env['calendar.event']
        event_vals = {
            'name': 'Formation Odoo',
            'start_date': training_date,
            'stop_date': training_date,
            'employee_id': employee.id
        }
        event = Event.create(event_vals)
        return super(SaleOrder, self).action_confirm()
