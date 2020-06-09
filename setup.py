import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012020S1P06',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description="# Package P06\r\nThis application was developed in resolution to the Women's Legal Service South Australia's current data collection process. This application will streamline data collection and provide a neat, accessible and easy to use online Client Advice Form for clients to fill out, removing the need for volunteers to call and obtain the client's preliminary information via the phone. This in turn will free up valuable resources, provide an efficient administrative data collection process and allow the Women's Legal Service South Australia to efficiently and effectively provide assistance to women in need in our communities. ",
      long_description_content_type='text/markdown',
      author='Zoe Johnston',
      author_email='john1068@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://github.com/LLAW3301/docassemble-LLAW33012020S1P06',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012020S1P06/', package='docassemble.LLAW33012020S1P06'),
     )

