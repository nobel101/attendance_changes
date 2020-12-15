# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from odoo import models, fields, api, exceptions, _


class CheckAttend(models.Model):
    _inherit = 'hr.attendance'

    attendance_type = fields.Selection([('check_in', 'Checked In'),
                                        ('check_out', 'Checked Out')], default='check_out')
    coupled_check = fields.Char()

    # TODO:check if check_in - now != 2 minutes if true raise error "you can't check in now please wait"
    @api.constrains('check_out', 'check_in', )
    def _check_in_time_interval(self):
        for attendance in self:
            if attendance.check_in and attendance.check_out:
                # TODO: Date format
                dt_format = '%Y-%m-%d %H:%M:%S'
                # TODO:
                enter = str(attendance.check_in)
                now = str(datetime.now().strftime(dt_format))
                interval = datetime.strptime(now, dt_format) - datetime.strptime(enter, dt_format)
                if interval < timedelta(minutes=2):
                    raise exceptions.ValidationError(_("Please wait unit your two minutes pass"))

    @api.model
    def _cron_check_in_out_coupling(self):
        # TODO: create a container list
        couple = []
        # TODO: loop over the two fields self.check_in and self.check_out
        for attend in self:
            # TODO: check if the check_in and check_out fields are set
            if attend.check_in and attend.check_out:
                # TODO: append the two fields to the container
                couple.append(attend.check_in)
                couple.append(attend.check_out)
        # TODO: slice the container to get couples
        coupled = list(zip(couple, couple[1:] + couple[:2]))
        print(coupled)
        # TODO: return the sliced list
        return {
            'xml_id': 'coupled_checks_attendance_action',
            'name': _('coupled checks tree view'),
            'view_type': 'tree',
            'view_mode': 'tree',
            'view_id': self.env.ref('coupled_checks_attendance_tree_view').id,
            'res_model': 'hr.attendance',
            'type': 'ir.actions.act_window',
        }
