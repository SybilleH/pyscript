print('Analyse my Data')


import numpy
import matplotlib.pyplot


def analyze(filename):
	data = numpy.loadtxt(fname=filename, delimiter=',')
	
	fig = matplotlib.pyplot.figure(figsize=(10,3))

	axes1=fig.add_subplot(1,3,1)
	axes2=fig.add_subplot(1,3,2)
	axes3=fig.add_subplot(1,3,3)





#-----------------------------------------
def centre(data, desired=0, exaggerate=1):
	#re-centres data around the desired value
	return((data-numpy.mean(data))*exaggerate) + desired

def fence(word, extension='*'):
	var=extension + word + extension
	return var

print(fence(extension='+', word='example'))

#-----------------------------------------------------

def abbrev(word):
	first_letter=word[0]
	second_letter=word[-1]	

	if len(word) <2:
		return first_letter
	else: 
		
		return first_letter+second_letter

print(abbrev('unicorn'))
print(abbrev('Stalin'))
print(abbrev('X'))

#----------------------------------------------------

#Git; 







