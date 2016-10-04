from django.core.management.base import BaseCommand
import logging

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        logging.debug("TESTING COMMANDS AND CELERY")