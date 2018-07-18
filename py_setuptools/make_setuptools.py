from __future__ import print_function
#
from setuptools import setup, Extension
# modified calls
from setuptools.command.install import install
from setuptools.command.build_ext import build_ext
#
import sys
import os
import subprocess
# partial
from functools import partial

settings = {

    'command' : 'make',
    'cmd_path' : None,
}


def compile_software(*args, **kwargs):
    """
    Used subprocess module to execute the command
    to compile/install your libraries
    """
    # execute the command
    if settings['cmd_path'] is None:
        path = os.getcwd()
    else:
        path = settings['cmd_path']
    # 
    subprocess.check_call(settings['command'], cwd=path, shell=True)


class CustomInstall(install, object):
    """Custom handler for the 'install' command"""

    def run(self):
        compile_software()
        super(CustomInstall, self).run()

class CustomBuildExt(build_ext, object):
    """Custom handler for the 'install' command"""

    def run(self):
        compile_software()
        super(CustomBuildExt, self).run()

setup = partial(setup, cmdclass= {
    'install' : CustomInstall,
    'build_ext' : CustomBuildExt,
    })
