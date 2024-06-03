# management/commands/backup_db.py

import os
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Backup the database'

    def handle(self, *args, **kwargs):
        db_settings = settings.DATABASES['default']
        db_name = db_settings['NAME']
        db_user = db_settings['USER']
        db_password = db_settings['PASSWORD']
        db_host = db_settings['HOST']
        db_port = db_settings['PORT']

        backup_file = f"{db_name}_backup.sql"

        command = f'pg_dump --dbname=postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name} > {backup_file}'
        os.system(command)

        self.stdout.write(self.style.SUCCESS(f'Successfully backed up database to {backup_file}'))
