A fork to run the tictactoe example on dotcloud.
================================================

Much thanks to these resources:

Ken Cochrane
http://kencochrane.net/blog/2012/03/deploying-a-django-application-on-dotcloud/
https://github.com/kencochrane/python-on-dotcloud

Cody Soyland:
http://www.youtube.com/watch?v=nocGRsytBkk

The Gevent-Socketio Django example:
https://github.com/abourget/gevent-socketio/tree/master/examples/django_chat


to run locally
---------------

#. Ensure you have libevent install
#. python wsgi.py


to deploy to dotcloud
----------------------

from this dir:

	dotcloud create tictactoe
	dotcloud push
