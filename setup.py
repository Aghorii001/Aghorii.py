from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name = "Aghorii.py",
    version = "3.0.4",
    url = "https://github.com/Slimakoi/Amino.py",
    download_url = "https://github.com/Aghorii001/Aghorii.py/tarball/master",
    license = "Apachhe",
    author = "Aghorii001",
    author_email = "rabin246808644@gmail.com",
    description = "A library to create Amino bots.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = [
        "aminoapps",
        "amino-py",
        "amino",
        "amino-bot",
        "narvii",
        "api",
        "python",
        "python3",
        "python3.x",
        "Aghorii001",
        "ravii"
    ],
    install_requires = [
        "setuptools",
        "requests",
        "six",
        "websockets",
        "websocket-client==1.3.1",
        "aiohttp"
    ],
    setup_requires = [
        "wheel"
    ],
    packages = find_packages()
)
