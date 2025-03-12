{
    'name': 'GPT Timesheet Grid View',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Adds a grid view to the Timesheet module',
    'author': 'Josh Taylor',
    'depends': ['hr_timesheet'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_timesheet_grid_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
