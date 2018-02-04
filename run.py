#!/usr/bin/env python
import sys
import getopt
from app import app


def command_help():
    print 'Usage: run.py [options]\n'
    print 'Options:'
    processor_option = '\t-h, --host    Host binding IP[127.0.0.1]'
    print processor_option
    print '\t-p, --port    Port[5000]'
    print '\t-h, --help    Help'
    sys.exit(1)


options, remainder = getopt.getopt(sys.argv[1:],
                                   'h:p:h', ['host=', 'port=', 'help'])
host = '127.0.0.1'
port = app.config['PORT']
for o, p in options:
    if o in ['-h', '--host']:
        host = p
    elif o in ['-p', '--port']:
        port = int(p)
    else:
        command_help()


app.run(host=host, port=port)
