import odoo

def update_calendar_view(order):
    ############################################
    # Se connecter à Odoo
    ########################################################
    odoo.api.Environment.manage().connect()

    ##########################################################################
    # Récupérer la ligne de commande correspondant à la formation vendue
    #######################################################################
    order_line = odoo.env['sale.order.line'].search([
        ('order_id', '=', order.id),
        ('product_id.is_training', '=', True),
    ])
    ##########################################################################
    # Mettre à jour la vue du calendrier avec les dates de la formation
    ###################################################################
    event = odoo.env['calendar.event'].search([
        ('training_id', '=', order_line.id),
    ])
    event.write({
        'start_date': order_line.start_date,
        'stop_date': order_line.end_date,
    })
#########################################################################################
# Lier la fonction de mise à jour de la vue du calendrier à l'événement "vente validée"
######################################################################################
odoo.on_record_write(update_calendar_view, 'sale.order')
