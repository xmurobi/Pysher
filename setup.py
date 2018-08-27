from setuptools import setup

VERSION = "1.0.0"

requirements = ["websocket-client>0.48"]


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="Pysher",
    version=VERSION,
    description="Pusher websocket client for python, based on Erik Kulyk's PythonPusherClient",
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords="pusher websocket client",
    author="Erik Kulyk",
    author_email="23okrs20+github@mykolab.com",
    license="MIT",
    url="https://github.com/nlsdfnbch/Pysher",
    install_requires=requirements,
    packages=["pysher"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries ',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
