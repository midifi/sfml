#!/usr/bin/env python

import subprocess, os

packages = ['system', 'window', 'graphics']

template = '''
Name: sfml-{pkg}
Description: Felix bindings for SFML (Simple Fast Multimedia Library) {pkg}.
provides_dlib: {libs}
provides_slib: {libs}
'''.strip()

basedir = os.path.dirname(__file__)

def write(pkg, libs, directory=None):
    if directory == None:
        directory = os.path.join(basedir, 'sfml-fpc')
    with open(os.path.join(directory, 'sfml-%s.fpc' % pkg), 'w') as f:
        f.write(template.format(pkg=pkg, libs=libs) + '\n')

if __name__ == '__main__':
    for pkg in packages:
        libs = subprocess.check_output(['pkg-config', '--libs', 'sfml-' + pkg]).\
              decode('ascii').strip()
        write(pkg, libs)
