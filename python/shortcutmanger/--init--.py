"""
Shortcut Manager
~~~~~~~~~~~~~~

an advance asyncio database wrapper

:copyright: (c) 2025 iVoid1

:license: MIT, see LICENSE for more details.
"""

__title__ = "hyper-database"
__author__ = "iVoid1"
__license__ = "MIT"
__copyright__ = "Copyright 2025 iVoid1"
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
