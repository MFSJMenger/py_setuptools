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

global_command = 'make'

def compile_software(command='make', *args, **kwargs):
    """
    Used subprocess module to execute the command
    to compile/install your libraries
    """
    # execute the command
    path = os.getcwd()
    # 
    subprocess.check_call(command, cwd=path, shell=True)


class CustomInstall(install):
    """Custom handler for the 'install' command"""

    def run(self):
        compile_software(command=global_command)
        super().run()

class CustomBuildExt(build_ext):
    """Custom handler for the 'install' command"""

    def run(self):
        compile_software(command=global_command)
        super().run()

setup = partial(setup, cmdclass= {
    'install' : CustomInstall,
    'build_ext' : CustomBuildExt,
    })
