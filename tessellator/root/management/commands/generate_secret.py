from ConfigParser import RawConfigParser
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import string
from tessellator.settings import CONFIG_FILE

class Command(BaseCommand):
    help = '''Generates a secret key for use in production.

Warning: This reads, parses, and writes the .ini file. It will not preserve 
comments or ordering.'''

    def generate_secret(self):
        chars = string.ascii_lowercase + string.digits + '!@#$%^&*()'
        return get_random_string(50, chars)

    def handle(self, *args, **options):
        cfg = RawConfigParser()
        cfg.read(CONFIG_FILE)
        
        if not cfg.has_section('APP'):
            cfg.add_section('APP')

        cfg.set('APP', 'SECRET_KEY', self.generate_secret())
        cfg.write(open(CONFIG_FILE, 'w'))
        
        self.stdout.write('Successfully updated SECRET_KEY in %s' % CONFIG_FILE)
