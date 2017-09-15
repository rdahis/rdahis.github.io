
from subprocess import call
import platform
import shutil, os

system = platform.system()

person = ''

if person == '':
	path_build = '/path/to/main_paper'
	path_sources = '/path/to/data_sources/data_set'

if system == 'Windows':
	pass
else:
	# Clears Input
	folder = '/input'
	shutil.rmtree(path_build+folder)
	os.mkdir(path_build+folder)

	# Copies Data
	call(['cp', path_sources+'/.dta', path_build+'/input'])

