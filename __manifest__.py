{
    'name': 'Check attendance module',
    'version': '13.0.1.1.0',
    'author': 'by omar khaled',

    'category': 'Uncategorized',
    'license': 'AGPL-3',
    'website': "www.example.com",
    'depends': ['base', 'hr_attendance'],
    'data': [
        'views/view.xml',
        'data/cron_job.xml',
    ],
    'auto_install': False,
    'installable': True,
}