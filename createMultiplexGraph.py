import pandas as pd 

f1 = pd.read_csv("ByMonthNoWeek/2012/avg_email_week/2012-01-type1", header=None)
f2 = pd.read_csv("ByMonthNoWeek/2012/reply_send/2012-01-type2", header=None)
f3 = pd.read_csv("ByMonthNoWeek/2012/ask_send/2012-01-type3", header = None)

file = open("multiplex.net", 'w')
file.write("# A network in multiplex format\n")
file.write("*Intra\n")
file.write("# layer node node weight\n")

i = 0
while i < (len(f1[0])+len(f2[0])+len(f3[0])):
	if i < len(f1[0]):
		file.write(str(1)+ " " + str(f1[0][i]) + " " + str(f1[1][i]) + " " + str(f1[2][i]) + "\n")
	elif i < (len(f1[0])+len(f2[0])):
		file.write(str(2)+ " " + str(f2[0][i-len(f1[0])]) + " " + str(f2[1][i-len(f1[0])]) + " " + str(f2[2][i-len(f1[0])]) + "\n")
	else:
		file.write(str(3)+ " " + str(f3[0][i-len(f1[0]) - len(f2[0])]) + " " + str(f3[1][i-len(f1[0]) - len(f2[0])]) + " " + str(f3[2][i-len(f1[0]) - len(f2[0])]) + "\n")
	i += 1