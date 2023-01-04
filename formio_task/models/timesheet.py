from odoo import api, fields, models, _

class Timesheet(models.Model):
    _inherit = 'account.analytic.line'
    form_id = fields.Many2one('formio.form','Form',compute="_create_form_to_attach",store=True,readonly=True)
    # user will select the task and save, the associated form will pop up
    @api.depends('task_id')
    def _create_form_to_attach(self):
        for rec in self:
            if rec.task_id.associated_form_template:
                details = {
                    'builder_id' : rec.task_id.associated_form_template.id ,
                    'title' : rec.task_id.associated_form_template.title + "-" + (self.partner_id.name or "" ),
                    'res_id': rec.task_id.id,
                    'timesheet_id': rec.id,
                }
            #     # create a form and attach to timesheet

                frm = self.env['formio.form'].create(details)
                # import wdb; wdb.set_trace()
                self.form_id = frm
        # pass


    # once form attached to timesheet, the task should not change(maybe)

    # on submission the description from feedback should go to timesheet

    # fill form button and open form button to be created
    # def action_fill_form(self):
    #     self.ensure_one()
    #     res_model_id = self.env.ref('project.model_project_task').id
    #     return {
    #         'name': 'Forms',
    #         'type': 'ir.actions.act_window',
    #         'domain': [('res_id', '=', self.id), ('res_model_id', '=', res_model_id)],
    #         'context': {'default_res_id': self.id},
    #         'view_type': 'form',
    #         'view_mode': 'kanban,tree,form',
    #         'res_model': 'formio.form',
    #         'view_id': False,
    #     }
    def action_view_formio(self):
        self.ensure_one()
        view_id = self.env.ref('formio.view_formio_form_formio').id
        if not self.form_id:
            return
        # import wdb; wdb.set_trace()
        frm = self.form_id.id
        return {
            "name": self.name,
            "type": "ir.actions.act_window",
            "res_model": "formio.form",
            # "view_id":,
            "views": [(view_id, 'formio_form')],
            "view_mode": "formio_form",
            "target": "current",
            "res_id": frm,
            "context": {}
        }
        # pass
