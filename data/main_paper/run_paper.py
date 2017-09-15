
from subprocess import call
import platform

system = platform.system()

person = ''

if person == '':
	path = '/path/to/main_paper'

if system == 'Windows':
	pass
else:
	print "//-- Runs Build --//"
	call(['python', path+'/build/code/run_directory.py'])
	print "//-- Runs Analysis --//"
	call(['python', path+'/analysis/code/run_directory.py'])
	print "//-- Compiles TeX --//"
	call(['latexmk', path+'/tex/paper/main_article.tex')

	print "Congratulations, you have a shiny new paper!"





