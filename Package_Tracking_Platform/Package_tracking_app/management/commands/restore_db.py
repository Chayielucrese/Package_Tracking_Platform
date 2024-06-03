# management/commands/restore_db.py

import os
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Restore the database from a backup file'

    def add_arguments(self, parser):
        parser.add_argument('backup_file', type=str, help='The backup file to restore from')

    def handle(self, *args, **kwargs):
        backup_file = kwargs['backup_file']
        db_settings = settings.DATABASES['default']
        db_name = db_settings['NAME']
        db_user = db_settings['USER']
        db_password = db_settings['PASSWORD']
        db_host = db_settings['HOST']
        db_port = db_settings['PORT']

        command = f'psql --dbname=postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name} < {backup_file}'
        os.system(command)

        self.stdout.write(self.style.SUCCESS(f'Successfully restored database from {backup_file}'))
