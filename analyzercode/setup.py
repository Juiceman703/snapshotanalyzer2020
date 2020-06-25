from setuptools import setup
setup(
    name='snapshotanalyzer',
    version='0.1',
    author="Juice703",
    author_email="hairmonster@gmail.com",
    description="Snapshotanalyzer is a tool to manage snapshots and instances",
    license="GPLv3+",
    packages=['analyzercode'],
    install_requires=[
        'click',
        'boto3',
    ],
    entry_points='''
        [console_scripts]
        snapshotanalyzer=analyzercode.snapshotanalyzer:cli
    ''',
)