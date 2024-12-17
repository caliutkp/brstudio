from odoo import models, fields, api

class StudioFieldTypeManager(models.Model):
    _name = 'studio.field.type'
    _description = 'Field Type Management'
    
    name = fields.Char(string='Display Name', required=True)
    technical_name = fields.Char(string='Technical Name', required=True)
    category = fields.Selection([
        ('basic', 'Basic'),
        ('numeric', 'Numeric'),
        ('relational', 'Relational'),
        ('special', 'Special')
    ], string='Category', required=True)
    
    # Field type properties
    has_size = fields.Boolean(string='Has Size Parameter')
    has_digits = fields.Boolean(string='Has Digits Parameter')
    has_relation = fields.Boolean(string='Has Relation')
    default_config = fields.Text(string='Default Configuration')
    
    _sql_constraints = [
        ('technical_name_uniq', 'unique(technical_name)', 
         'Technical name must be unique!')
    ]
    
    @api.model
    def get_type_config(self, field_type):
        """Get configuration for field type"""
        type_record = self.search([('technical_name', '=', field_type)], limit=1)
        if type_record:
            return {
                'has_size': type_record.has_size,
                'has_digits': type_record.has_digits,
                'has_relation': type_record.has_relation,
                'default_config': type_record.default_config,
            }
        return {}