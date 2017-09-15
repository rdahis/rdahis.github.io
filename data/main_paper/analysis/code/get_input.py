
from subprocess import call
import platform
import os, shutil

system = platform.system()

person = ''

if person == '':
	path_build = '/path/to/main_paper/build'
	path_analysis = '/path/to/main_paper/analysis'

if system == 'Windows':
	pass
else:
	# Clears Input
	folder = '/input'
	shutil.rmtree(path_analysis+folder)
	os.mkdir(path_analysis+folder)

	# Copies Input
	call(['cp', '-R', path_build+'/output/.', path_analysis+'/input'])


