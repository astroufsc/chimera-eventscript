from distutils.core import setup

setup(
    name='chimera_eventscript',
    version='0.0.1',
    packages=['chimera_eventscript', 'chimera_eventscript.controllers'],
    scripts=[],
    url='http://github.com/astroufsc/chimera-eventscript',
    license='GPL v2',
    author='William Schoenell',
    author_email='wschoenell@gmail.com  ',
    description='Chimera template that runs scripts when events are triggered by an instrument.'
)
