from odoo import api, models, _, fields
from odoo.exceptions import ValidationError
from erppeek import Client


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Ajoutez un champ de date de formation
    training_date = fields.Date('Date de formation')

    #Ajoutez un champ d'employé
    employee_id = fields.Many2one('hr.employee', string='Employé')

    #Montant
    amount = fields.Float('Montant dapprobation')

    #Déclaration d'un nouveau champ de type Many2one qui pointe vers le modèle de groupe d'Odoo (res.groups)
    manager_group_id = fields.Many2one('res.groups', string='Groupe de gestionnaire')

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
        if self.amount > self.partner_id.max_allowed_amount:
            raise ValidationError("Le montant de la commande de vente est supérieur au montant maximal autorisé pour le partenaire.")
        event = Event.create(event_vals)
        return super(SaleOrder, self).action_confirm()
    
    #Fonction qui vérifie si la probation est nécessaire 
    def requires_approval(self):
        amount = self.amount
        manager_group = self.manager_group_id.name
        if amount < 500:
            return False
        elif 500 <= amount < 2000:
            return manager_group in ['group_manager_level_1', 'group_manager_level_2', 'group_manager_level_3']
        elif 2000 <= amount < 5000:
            return manager_group in ['group_manager_level_2', 'group_manager_level_3']
        else:
            return manager_group == 'group_manager_level_3'