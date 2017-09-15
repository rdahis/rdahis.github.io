
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
		shutil.rmtree(path+'/analysis'+folder)
		os.mkdir(path+'/analysis'+folder)

        print "Gets Input"
        call(['python', path+'/analysis/code/get_input.py'])

	print "Executes Code"
	call(['stata-se', '-b', 'do' + '\"' + path+'/analysis/code/analysis.do'+'\" &'])
	for file in glob.glob(path+'/*.log'):
		os.remove(file)







