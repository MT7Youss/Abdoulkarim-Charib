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
    manager_group_id = fields.Many2one('res.groups', string='groupeDeGestionnaire')
    
    #Déclaration d'un nouveau champ de type Many2one qui pointe vers le modèle de groupe d'Odoo (res.users)
    manager_id = fields.Many2one('res.users', string='Manager')


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

    # Vérifiez si l'approbation est nécessaire
        if self.requires_approval():
        # Créez une activité pour le manager
            Activity = self.env['mail.activity']
            activity_vals = {
                'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                'note': 'Veuillez approuver cette commande de vente',
                'res_id': self.id,
                'res_model_id': self.env.ref('sale.model_sale_order').id,
                'user_id': self.env.user.id
        }
            activity = Activity.create(activity_vals)
        else:
            return super(SaleOrder, self).action_confirm()
    
    #Fonction qui vérifie si la probation est nécessaire 
    def requires_approval(self):
        amount = self.amount
        manager_group = self.env['res.groups'].search([('name', '=', 'groupeDeGestionnaire')])
        if amount < 500:
            return False
        elif 500 <= amount < 2000:
            return manager_group.name == 'groupeDeGestionnaire'
        elif 2000 <= amount < 5000:
            return manager_group.name == 'groupeDeGestionnaire'
        else:
            return manager_group.name == 'groupeDeGestionnaire'

    @api.multi
    def request_approval(self):
        # Récupérez le premier manager disponible
        available_managers = self.env['res.users'].search([('groups_id', '=', 'groupeDeGestionnaire')])
        if available_managers:
            manager = available_managers[0]
        else:
            raise ValidationError("Il n'y a pas de manager disponible pour approuver cette commande de vente.")

        # Créez une activité pour le manager
        self.activity_schedule(
        'mail.mail_activity_data_warning',
        user_id=manager.id,
        note=_('Demande d\'approbation de commande de vente'),
        summary='Demande d\'approbation de commande de vente'
    )

        # Enregistrez le manager sélectionné dans le champ manager_id
        self.manager_id = manager    
		