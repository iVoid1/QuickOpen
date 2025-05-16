"""
Quick Open
~~~~~~~~~~~~~~

A simple tool for quickly opening files, folders, or applications on Windows by creating and managing shortcuts.
This package provides a simple way to create and manage shortcuts to open applications, documents, images, or other commonly used files.
It supports creating shortcuts for files, folders, and applications, and allows you to specify custom icons and other properties, such as window state or working directory.
It also provides a simple command-line interface for creating and managing shortcuts, allowing users to add, remove, or list shortcuts easily. For example, you can use the command `quickopen add "MyApp" "C:\\Path\\To\\App.exe"` to create a shortcut for an application.
"""

__title__ = "shortcutmanger"
__author__ = "iVoid1"
# Placeholder, modified by dynamic-versioning.
__version__ = "0.0.0"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import Literal, NamedTuple

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int
    metadata: str


# Placeholder, modified by dynamic-versioning.
version_info: VersionInfo = VersionInfo(0, 0, 0, "final", 0, "")

logging.getLogger(__name__).addHandler(logging.NullHandler())