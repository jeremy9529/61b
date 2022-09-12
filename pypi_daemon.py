import os
import sys

BASEDIR = os.path.dirname(os.path.abspath(__file__))
if BASEDIR not in sys.path:
    sys.path.append(BASEDIR)

from lib.config import *
from utils.manage import *
from lib.clp import CommandLineParser
from lib.app import App
from eco.pypi.parser import PypiParser


def main(argv):
    if len(argv)==2 and argv[1]=='kill':
        kill_instances(os.path.basename(__file__))
        return

    if get_number_of_instances(os.path.basename(__file__)) > 1:
        print('Another instance of this script is already running.')
        print('To run a new instance, please kill all existent instances first with following cmd:')
        print('\t%s kill' % os.path.basename(__file__))
        return

    options = CommandLineParser(ECOSYSTEM_NAME_PYPI).parse()
    App(ECOSYSTEM_NAME_PYPI, LOG_FILENAME_PYPI, CACHE_FILENAME_PYPI, PypiParser(), options).run()


if __name__ == '__main__':
    main(sys.argv)
