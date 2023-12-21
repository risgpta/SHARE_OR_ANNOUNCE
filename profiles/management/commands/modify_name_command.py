# your_app_name/management/commands/your_custom_cleanup_command.py
from django.core.management.base import BaseCommand
from profiles.models import Profiles


class Command(BaseCommand):
    help = 'Your custom cleanup command description'

    def handle(self, *args, **options):
        # Your cleanup logic goes here
        profiles = Profiles.objects.all()
        c = 0
        for p in profiles:
            c = c + 1
            if c > 15:
                p.delete()
            else:
                p.first_name = p.email+"_ui-"+str(c)
                p.last_name = p.email+str(c)
                p.save()
        self.stdout.write(self.style.SUCCESS('Cleanup completed successfully'))
