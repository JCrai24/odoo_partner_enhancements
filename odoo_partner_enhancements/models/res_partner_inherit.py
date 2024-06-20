from odoo import models, fields

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    
    """
    Attempted to use the 'domain' attribute within the inherited view but failed to make it work.
    Used this computed field instead of putting constraints on the original sale_order_ids field used 
    by the parent model. 
    """
    current_sale_order_ids = fields.One2many(
        'sale.order',
        compute='_compute_current_sale_order_ids',
        store=False,
        string="Current Sales Orders"
    )
    
    
    def _compute_current_sale_order_ids(self):
        """
        Compute method to populate the 'current_sale_order_ids' field.
        Filters to show sales orders that are current by removing completed and cancelled sales orders
        """
        for partner in self:
            partner.current_sale_order_ids = partner.sale_order_ids.filtered(lambda order: order.state not in ('done', 'cancel'))
