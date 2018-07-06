try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'my test project',
    'author':'lpc',
    'url':'www.lpcrin.com',
    'download_url':'where',
    'author_email':'dsda@ll.com',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'NAME'
}

setup(**config)