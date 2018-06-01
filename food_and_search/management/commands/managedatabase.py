from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Use the command --chargedatabase, to load the database or use, for example --updatedatabase in a cron to update it'


    def add_arguments(self, parser):

        parser.add_argument(
            '--chargedatabase',
            action='store_true',
            dest='charge_database',
            help='To load the database or use',
        )
        parser.add_argument(
            '--updatedatabase',
            action='store_true',
            dest='update_database',
            help='Update database ,for example updatedatabase in a cron to update it',
        )

    def handle(self, *args, **options):
        if options['charge_database']:
            self.stdout.write('charge database')

        if options['update_database']:
            self.stdout.write('update database')
