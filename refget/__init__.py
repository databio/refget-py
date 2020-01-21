# Project configuration, particularly for logging.

import logging
from ._version import __version__
from .hash_functions import *
from .refget import RefDB, RedisDict, MongoDict
from .refget import fasta_checksum, parse_fasta

__classes__ = ["RefDB", "RedisDict", "MongoDict"]
__all__ = __classes__ + []
