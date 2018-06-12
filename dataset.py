import string
import numpy as np
from collections import OrderedDict

def lecturaDatos(fileE):
	f=open(fileE,'r')
	line=f.readline()
 	att=OrderedDict()
 	ds = dataset() 	
 	ds.data = []
	ds.target = []
	ds.feature_names = []
	ds.target_names = []  
	while string.find(line,"@data")<0:
		if string.find(line,"@attribute")>=0 and string.find(line,"real")>=0:
			line=string.split(line)
			minimo=string.split(line[3],"[")
			minimo=float(string.split(minimo[1],",")[0])
			maximo=float(string.split(line[4],"]")[0])
			attAux={line[1]: [minimo, maximo]}
			att.update(attAux)
		elif string.find(line,"@attribute")>=0 and string.find(line,"real")<0:
			line=string.split(line)
			values = []
			#count = 0
			for l in line[2:]:
				#if count > 1:
					values.append(l)
				#count = count + 1
			attAux={line[1]:values}
			att.update(attAux)         
		elif string.find(line,"@output")>=0 or string.find(line,"@outputs")>=0:
                  clase = string.split(line)
                  clase = clase[1]
		line=f.readline()
	auxClases = att.pop(clase)
	clases = []
	c= auxClases.pop(0)
	c = string.split(c,"{")
	c = string.split(c[1],",")
	clases.append(c[0])
	c=auxClases.pop()
	c = string.split(c,",")
	c = string.split(c[0],"}")
	cLast = c[0] 
	for c1 in auxClases:
		c = string.split(c1,",")
		clases.append(c[0])	
	clases.append(cLast)	
	attAux={clase:clases}	
	att.update(attAux)
	line=f.readline()
	exClases = []
 	examples = []
	while line!="":
		line=line.replace(","," ")
		l=string.split(line)
		values = l[0:len(l)-1]
		val = []
		for v in values:
			val.append(float(v))
		#npVal = np.array(val)
		examples.append(val)
		#examples = np.concatenate([examples, npVal])
		exClases.append(att[clase].index(l[len(l)-1]))
		#exClases.append(l[len(l)-1])       
		line=f.readline()
 	examples = np.array(examples)	
 	f.close()
 	ds.data = examples
 	ds.target = np.array(exClases)
 	ds.feature_names = att.keys()[:-1]
 	ds.target_names = att['Class']
 	return ds

class dataset:
    data = []
    target = []
    feature_names = []
    target_names = []
