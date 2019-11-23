#!/usr/bin/env python3
# 
# Krew, an easily accessible HTTP Server for Linux Machines
# Copyright (C) 2019  Adrian Gjerstad
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Krew, an easily accessible HTTP Server for Linux Machines

This program creates an HTTP Server using Python 3 code, which can be seen
starting below this docstring.

NOTICE: This program may be used with imports to create your own derivatives of
Krew, so information on how to do this can be found in the Wiki on GitHub.
"""

from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import sys
import os

__author__ = 'Adrian Gjerstad'
__copyright__ = 'Copyright (C) 2019  Adrian Gjerstad'
__credits__ = [
  'Adrian Gjerstad'
]

__license__ = 'GNU GPLv3'
__version__ = '0.0.1'
__maintainer__ = 'Adrian Gjerstad'
__email__ = 'Not listed'
__status__ = 'Prototype'

__interactive__ = sys.stdout.isatty() and sys.stderr.isatty()

################################################################################
############################## KrewRequestHandler ##############################
################################################################################

class KrewRequestHandler(BaseHTTPRequestHandler):
  pass

################################################################################
################################## KrewServer ##################################
################################################################################

class KrewServer(ThreadingHTTPServer):
  pass

################################################################################
############################ KrewInteractiveProcess ############################
################################################################################

def KrewInteractiveProcess():
  while True:
    sys.stderr.write('\033[s>' % (platform._node()))

################################################################################
################################ KrewMainMethod ################################
################################################################################

def KrewMainMethod():
  if __interactive__:
    sys.stderr.write('''Krew Copyright (C) 2019  Adrian Gjerstad
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
    ''')

################################################################################
################################ __name__ Guard ################################
################################################################################

if __name__ == '__main__':
  try:
    KrewMainMethod()
  except BaseException:
    if __interactive__:
      sys.stderr.write(
        '\033[H\033[2J\033[31mAn internal uncaught fatal ' +
        'exception occurred while running.\n\n'
      )

      from traceback import print_exc
      print_exc()

      sys.stderr.write('\033[0m')

################################################################################
################################# Custom Guard #################################
################################################################################

else:
  del KrewMainMethod
  del __interactive__
