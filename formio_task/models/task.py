# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from odoo import api, fields, models, _


class TaskProject(models.Model):
    _inherit = 'project.task'

    formio_forms = fields.One2many('formio.form','task_id', string='Forms')
    associated_form_template = fields.Many2one('formio.builder', string='Form Template')
    formio_forms_count = fields.Integer(
        compute='_compute_formio_forms_count', compute_sudo=True, string='Forms Count')
    formio_this_model_id = fields.Many2one(
        'ir.model', compute='_compute_formio_this_model_id', compute_sudo=True)

    def _compute_formio_forms_count(self):
        for r in self:
            r.formio_forms_count = len(r.formio_forms)

    def _compute_formio_this_model_id(self):
        self.ensure_one()
        model_id = self.env.ref('project.model_project_task').id
        self.formio_this_model_id = model_id

    def write(self, vals):
        # Simpler to maintain and less risk with extending, than
        # computed field(s) in the formio.form object.
        res = super(TaskProject, self).write(vals)
        if self.formio_forms:
            form_vals = self._prepare_write_formio_form_vals(vals)
            if form_vals:
                self.formio_forms.write(form_vals)
        return res

    def _prepare_write_formio_form_vals(self, vals):
        if vals.get('name'):
            form_vals = {
                'res_name': self.name
            }
            return form_vals
        else:
            return False

    def action_formio_forms(self):
        self.ensure_one()
        res_model_id = self.env.ref('base.model_res_partner').id
        return {
            'name': 'Forms',
            'type': 'ir.actions.act_window',
            'domain': [('res_id', '=', self.id), ('res_model_id', '=', res_model_id)],
            'context': {'default_res_id': self.id},
            'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'res_model': 'formio.form',
            'view_id': False,
        }
