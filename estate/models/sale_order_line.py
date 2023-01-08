from odoo import api, fields, models, Command

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Ajoutez un champ de date de formation
    training_date = fields.Date('Date de formation')

    # Ajoutez un champ d'employé
    employee_id = fields.Many2one('hr.employee', string='Employé')

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