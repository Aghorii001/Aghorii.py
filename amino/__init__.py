__title__ = "Aghorii.py"
__author__ = "Aghorii001"
__license__ = "Apache"
__copyright__ = "Copyright 2020-2022 Aghorii"
__version__ = "3.0.4"

from .acm import ACM
from .client import Client
from .sub_client import SubClient
from .socket import Callbacks, SocketHandler

from .async_acm import AsyncACM
from .async_client import AsyncClient
from .async_sub_client import AsyncSubClient
from .async_socket import AsyncCallbacks, AsyncSocketHandler

from .lib.util import device, exceptions, headers, helpers, objects

from requests import get
from json import loads

__newest__ = loads(get("https://pypi.python.org/pypi/Aghorii.py/json").text)["info"]["version"]

if __version__ != __newest__:
    print(exceptions.LibraryUpdateAvailable(f"New version of {__title__} available: {__newest__} (Using {__version__})"))
