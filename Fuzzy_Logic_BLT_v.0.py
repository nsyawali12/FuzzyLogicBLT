#Kamus IMPORT
import random
import math

#############

tester = ("Hello World! ")
print (tester)

project = ("Tugas 2 Artificial Intelligence : Fuzzy_Logic ")
print (project)

def RuleIncome(Income):
	if ( Income < 0.5 ) :
		Ki = ('Kecil')
	elif ( (Income > 0.5) and ( Income <= 0.7 ) ):
		Ki = ('Kecil')
	elif ( (Income < 0.7 ) and (Income > 1.2 ) ):
		Ki = ('Sedang')
	elif ( (Income > 1.2 ) and (Income <= 1.4) ):
		Ki = ('Sedang')
	elif ( (Income > 1.4 ) and (Income <= 1.9) ):
		Ki = ('Besar')
	elif ( Income > 1.9 ):
		Ki = ('Besar')


