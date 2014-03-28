"""
RenameBBProject.py Copyright (C) 2014  Daniel San Ferreira da Rocha <daniel.samrocha@gmail.com>

RenameBBProject.py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

RenameBBProject.py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with RenameBBProject.py. If not, see <http://www.gnu.org/licenses/>.
"""

#!/usr/bin/python

import os
import os.path

old_name = raw_input('Insert current project name: ')
new_name = raw_input('Insert new project name: ')

new_name = new_name[0].upper() + new_name[1:]

os.rename('./' + old_name + '.pro', './' + new_name + '.pro')
os.rename('./translations/' + old_name + '.pro', './translations/' + new_name + '.pro')
os.rename('./translations/' + old_name + '.ts', './translations/' + new_name + '.ts')

def changeProjectName(arg, dir_name, file_names):
    for file_name in file_names:
        file_name = dir_name + '/' + file_name
        print 'File name: ', file_name
        if (os.path.isfile(file_name)):
            current_file = open(file_name)
            content = current_file.read()
            current_file.close()
            open(file_name, 'w').close()
            current_file = open(file_name, 'w')
            content = content.replace(old_name, new_name)
            content = content.replace(old_name.lower(), new_name.lower())
            current_file.write(content)
            current_file.close()

os.path.walk('.', changeProjectName, '')