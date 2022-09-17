from distutils.core import setup
from xml.etree.ElementInclude import include
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['ts_semantic_inference'],
    package_dir={'': 'src'},
    include={'': 'include'}
)

setup(**setup_args)