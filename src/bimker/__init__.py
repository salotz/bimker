# -*- coding: utf-8 -*-

"""Top-level package."""

from ._version import __version__

__author__ = "Samuel D. Lotz"
__email__ = 'samuel.lotz@salotz.info'


# module stuff
import os.path as osp

CONFIG_DIR = osp.expanduser(osp.expandvars("$HOME/.bimker"))
