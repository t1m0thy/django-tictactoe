#!/usr/bin/env python
import gevent
from gevent import monkey
monkey.patch_all()

from socketio.server import SocketIOServer
import django.core.handlers.wsgi
import os
import sys


#===============================================================================
# BEGIN PATCH 
#===============================================================================
def log_request(self):
    """
    Patch for logging from http://stackoverflow.com/questions/9444405/gunicorn-and-websockets
    """
    log = self.server.log
    if log:
        if hasattr(log, "info"):
            log.info(self.format_request() + '\n')
        else:
            log.write(self.format_request() + '\n')

gevent.pywsgi.WSGIHandler.log_request = log_request
#===============================================================================
# END PATCH
#===============================================================================



try:
    import settings
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

application = django.core.handlers.wsgi.WSGIHandler()

sys.path.insert(0, os.path.join(settings.PROJECT_ROOT, "apps"))

if __name__ == '__main__':
    PORT = 9000
    print 'Listening on http://127.0.0.1:%s and on port 843 (flash policy server)' % PORT
    SocketIOServer(('', PORT), application, namespace="socket.io").serve_forever()
