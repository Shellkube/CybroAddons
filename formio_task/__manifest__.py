# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

{
    'name': 'Forms | Task',
    'summary': 'Forms integration with Task in Projects',
    'version': '1.1',
    'license': 'LGPL-3',
    'author': 'Nova Code',
    'website': 'https://www.novacode.nl',
    'live_test_url': 'https://demo15.novacode.nl',
    'category': 'Project',
    'depends': ['project', 'formio','hr_timesheet'],
    'data': [
        'data/formio_task_data.xml',
        'views/task_views.xml',
        'views/timesheet_views.xml',
        'views/formio_form_views.xml',
    ],
    'application': True,
    'images': [
        'static/description/banner.gif',
    ],
    'description': """
Forms | Task
===========

"""
}
