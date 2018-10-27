#Kamus IMPORT
import random
import math

#############

tester = ("Hello World! ")
print (tester)

project = ("Tugas 2 Artificial Intelligence : Fuzzy_Logic ")
print (project)


#Prosedur Aturan dari Pengelompokan Pendapatan

def RuleIncome(Income):
	if ( Income < 0.5 ) :
		Ki = ("Kecil")
	elif ( (Income > 0.5) and ( Income <= 0.7 ) ):
		Ki = ("Kecil")
	elif ( (Income < 0.7 ) and (Income > 1.2 ) ):
		Ki = ("Sedang")
	elif ( (Income > 1.2 ) and (Income <= 1.4) ):
		Ki = ("Sedang")
	elif ( (Income > 1.4 ) and (Income <= 1.9) ):
		Ki = ("Besar")
	elif ( Income > 1.9 ):
		Ki = ("Besar")

#Prosedur Aturan dari Pengelompokan Hutang
def RuleDebt(Debt):
	if ( Debt < 30):
		Kd = ("Kecil")
	elif ( ( Debt > 30) and (Debt <= 40) ):
		Kd = ("Kecil")
	elif ( (Debt > 40 ) and (Debt <= 70) ):
		Kd = ("Sedang")
	elif ( (Debt > 70 ) and (Debt <= 80) ):
		Kd = ("Sedang")
	elif ( (Debt > 80) and (Debt <= 98) ):
		Kd = ("Besar")
	elif ( (Debt > 98) ):
		Kd = ("Besar")

#Rule Pengelompokkan
#R1 = HasilRuleIncome
#R2 = HasilRuleDebt

def RuleDI(R1, R2):
	if( (R1 == "Kecil") and (R2 == "Kecil")):
		ResR = ("Sedang")
	elif ( (R1 == "Kecil") and (R2 == "Sedang") ):
		ResR = ("Tinggi")
	elif ( (R1 == "Kecil") and (R2 == "Tinggi")):
		ResR = ("Tinggi")

	elif ( (R1 == "Sedang") and (R2 == "Kecil")):
		ResR = ("Tinggi")
	elif ( (R1 == "Sedang") and (R2 == "Sedang")):
		ResR = ("Sedang")
	elif ( (R1 == "Sedang") and (R2 == "Tinggi")):
		ResR = ("Tinggi")

	elif ( (R1 == "Tinggi") and (R2 == "Kecil")):
		ResR = ("Kecil")
	elif ( (R1 == "Tinggi") and (R2 == "Sedang")):
		ResR = ("Kecil")
	elif ( (R1 == "Tinggi") and (R2 == "Sedang")):
		ResR = ("Sedang")





