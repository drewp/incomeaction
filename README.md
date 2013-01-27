incomeaction
============

incomeaction.org


maintenance
===========

repo
----
/var/www/ia is the production checkout that the site is served from
and the services are run from.

It is also the root of a python virtualenv.

web
---
/etc/apache2/httpd.conf has documentroot in /var/www/ia/www, which is
inside the git checkout

virtualenv
----------
The file ./pydeps is a manifest list for [virtualenv](http://www.virtualenv.org/en/latest/). To build the virtualenv for the first time:

    % virtualenv .

To update its contents to what pydeps says, which must be done if pydeps changed:

    % bin/pip install --requirement ./pydeps


supervisor
----------
/etc/init.d/supervisor is not used.

/etc/init/ia_supervisor.conf contains this:

    description	"incomeaction services"

    start on filesystem or runlevel [2345]
    stop on runlevel [!2345]

    respawn
    respawn limit 10 5
    umask 022

    exec /sbin/start-stop-daemon --chuid ia --exec /usr/bin/supervisord --start -- -c /var/www/ia/supervisord.conf

