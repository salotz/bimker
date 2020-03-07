from invoke import task, Collection

import os
import os.path as osp
from pathlib import Path
from contextlib import contextmanager

from . import (
    CONFIG_DIR,
)

import bimker.config as config

@contextmanager
def cd(newdir):
    """Context manager for changing directories to make sure you go back"""
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


def validate_locals(local_vars):

    assert 'bimker_program' in local_vars, \
        "the 'bimker_program' invoke Program not specific in tasks target"


assert config.tasks is not None, \
    "Bimker tasks target not specified"

# expand it then validate
tasks_target = Path(osp.expanduser(osp.expandvars(config.tasks)))

assert osp.exists(tasks_target), \
    f"Bimker tasks target not found: {tasks_target}"

# if it is a single file go ahead and read it.
if tasks_target.is_file():

    # open it and exec it
    with open(tasks_target) as rf:
        exec(rf.read())

# STUB: implement JIT when we actually want this
elif tasks_target.is_dir():
    raise NotImplementedError("Not supported yet")

# validate that it provided the right things
validate_locals(locals())

# this should have provided the bimker_program so we just alias it

program = bimker_program


# get the directory to execute things from
exec_dir = Path(osp.expanduser(osp.expandvars(config.exec_dir)))

assert osp.exists(exec_dir), \
    "Execution directory does not exist: {exec_dir}"
assert exec_dir.is_dir(), \
    "Execution directory is not a directory: {exec_dir}"

def cli():
    with cd(exec_dir):
        program.run()

if __name__ == "__main__":

    cli()
