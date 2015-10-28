CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/ilya/ask/ask_litik',
    'user': 'www-data',
    'group': 'www-data',
    'args': (
        '--bind=0.0.0.0:8001',
        '--workers=2',
        '--timeout=60',
        '--access-logfile=-',
        'hw_wsgi:application',
    ),
}
