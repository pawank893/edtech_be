from psycogreen.gevent import patch_psycopg

bind = "0.0.0.0:8002"

workers = 4

keepalive = 300
worker_tmp_dir = '/gunicorn-tmp'

worker_class = "gevent"
timeout = 300

loglevel = 'debug'

errorlog = "/var/log/edtech/gunicorn.error.log"
accesslog = "/var/log/edtech/gunicorn.access.log"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

proc_name = "edtech"


def post_fork(server, worker):
    # patch psycopg2 for gevent compatibility
    patch_psycopg()
