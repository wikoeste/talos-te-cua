from setuptools import setup

setup(
    name='cua-inject',
    version='0.2',
    packages=["cua","cua.common"],
    description='Cua Injection tool',
    author='Will Koester',
    author_email='wikoeste@cisco.com',
    url='',
    entry_points={
        'console_scripts':[
            'te-cuainject=cua.main:main',
            ],
        },
)