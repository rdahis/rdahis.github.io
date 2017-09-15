
from subprocess import call
import platform
import shutil, os, glob

system = platform.system()

person = ''

if person == '':
	path = '/path/to/main_paper'

if system == 'Windows':
	pass
else:
	print "Cleans Output and Temporary"
	for folder in ['/output', '/tmp']:
		shutil.rmtree(path+'/build'+folder)
		os.mkdir(path+'/build'+folder)

        print "Gets Input"
        call(['python', path+'/build/code/get_input.py'])

	print "Executes Code"
	call(['stata-se', '-b', 'do' + '\"' + path+'/build/code/build.do'+'\" &'])
	for file in glob.glob(path+'/*.log'):
		os.remove(file)



