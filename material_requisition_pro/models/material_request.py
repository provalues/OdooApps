from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MaterialRequisition(models.Model):
    _name = 'material.requisition'
    _description = 'Material Requisition'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    department_id = fields.Many2one('hr.department', string='Department', 
    compute='_compute_department_id', 
    store=True
        )
    request_date = fields.Date(string='Request Date', default=fields.Date.context_today, required=True)
    reason = fields.Text(string='Reason')
    priority = fields.Selection([
        ('high', 'High'),
        ('normal', 'Normal'),
        ('low', 'Low'),
    ], string='Priority', default='normal')
    line_ids = fields.One2many('material.requisition.line', 'requisition_id', string='Requisition Lines')
    # Approval fields and states
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('department_approval', 'Department Manager Approved'),
        ('procurement_approval', 'Procurement Manager Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True)
    
    @api.depends('employee_id')
    def _compute_department_id(self):
        for requisition in self:
            requisition.department_id = requisition.employee_id.department_id        
    

    def action_department_approval(self):
        self.state = 'department_approval'
    def action_submit(self):
        self.state = 'submit'

    def action_procurement_approval(self):
        if not self.env.user.has_group('material_requisition_pro.group_procurement_manager'):
            raise UserError(_('Only the procurement manager can approve this requisition.'))
        self.state = 'procurement_approval'
    def action_reject(self):
        self.state = 'rejected'        

class MaterialRequisitionLine(models.Model):
    _name = 'material.requisition.line'
    _description = 'Material Requisition Line'

    requisition_id = fields.Many2one('material.requisition', string='Material Requisition', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True, default=1.0)
    notes = fields.Text(string='Notes')
