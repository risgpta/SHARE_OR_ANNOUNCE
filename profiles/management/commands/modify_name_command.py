# your_app_name/management/commands/your_custom_cleanup_command.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Your custom cleanup command description'

    def handle(self, *args, **options):
        # Your cleanup logic goes here
        self.stdout.write(self.style.SUCCESS('Cleanup completed successfully'))
