{
    'name': 'GPT Timesheet Grid',
    'version': '1.0',
    'category': 'Human Resources',
    'author': 'Josh Taylor',
    'summary': 'Enhanced Timesheet Grid with Manager Approval and Mobile Optimization',
    'description': 'Adds grid view for weekly entries, manager approval, and mobile optimization.',
    'depends': ['hr_timesheet'],
    'data': [
        'views/timesheet_views.xml',
        'views/report_timesheet.xml',
        'views/mobile_views.xml',
        'data/timesheet_data.xml',
    ],
    'installable': True,
    'auto_install': False,
}
