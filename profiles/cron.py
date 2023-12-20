# your_app_name/cron.py
from django.core.management import call_command
from django_cron import CronJobBase, Schedule


class modify_name(CronJobBase):
    schedule = Schedule(run_every_mins=1)
    code = 'profiles.modify_name'  # a unique code

    def do(self):
        # Your cleanup operation or command goes here
        # For example, calling a management command
        call_command('modify_name_command')
