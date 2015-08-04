from distutils.core import setup

VERSION_FILE = 'version.txt'

# convert MarkDown to reStructuredText
try:
    import pypandoc
    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    LONG_DESCRIPTION = open('README.md').read()

# increment dynamic working number
VERSION = open(VERSION_FILE).read()


setup(
    name='litelog',
    version=VERSION,
    author='Matthew Cotton',
    author_email='matt@thecottons.com',
    py_modules=['litelog',],
    # scripts=[],
    url='http://pypi.python.org/pypi/litelog/',
    license='LICENSE.txt',
    description='Simplified, robust, selective, recursive logging utility for Python.',
    long_description=LONG_DESCRIPTION,
    install_requires=[],
)


def next_version(version):
    """Increments the version given trivially"""
    nums = (int(i) for i in version.split('.'))
    (start, last) = nums[:-1], nums[-1]
    last += 1
    return ''.join(start + (last,))

with open(VERSION_FILE, 'w') as FILE:
    FILE.write(next_version(VERSION))
