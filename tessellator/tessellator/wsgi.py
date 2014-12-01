"""
WSGI config for tessellator project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tessellator.settings")

activate_this = os.expandvars('$HOME/env/tessellator/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
