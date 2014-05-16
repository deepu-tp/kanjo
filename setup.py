try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Twitter Sentiment Analysis System',
    'author': 'Deepu T Philip',
    'url': '',
    'download_url': '',
    'author_email': 'deepu.dtp@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['kanjo'],
    'scripts': ['bin/kanjo_train'],
    'name': 'kanjo'
}

setup(**config)
