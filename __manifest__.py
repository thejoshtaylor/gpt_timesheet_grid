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
    'assets': {
        'web.assets_backend': [
            'gpt_timesheet_grid/static/src/model/grid_model.js',
            'gpt_timesheet_grid/static/src/renderer/grid_renderer.js',
            'gpt_timesheet_grid/static/src/view/grid_view.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
