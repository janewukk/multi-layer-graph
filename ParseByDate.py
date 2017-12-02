import pandas as pd


data = pd.read_csv("dataset/split_2012", header=None)
data1 = pd.read_csv("dataset/split_2013", header=None)
data2 = pd.read_csv("dataset/split_2014", header=None)
data3 = pd.read_csv("dataset/split_2015", header=None)
data4 = pd.read_csv("dataset/split_2016", header=None)

id_dict = {}
id1_f = list(set(data[0]))
id1_t = list(set(data[1]))
id2_f = list(set(data1[0]))
id2_t = list(set(data1[1]))
id3_f = list(set(data2[0]))
id3_t = list(set(data2[1]))
id4_f = list(set(data3[0]))
id4_t = list(set(data3[1]))
id5_f = list(set(data4[0]))
id5_t = list(set(data4[1]))
temp = [id1_f, id1_t, id2_f, id2_t, id3_f, id3_t, id4_f, id4_t, id5_t, id5_f]
id_set = set().union(*temp)

i = 1
for item in list(id_set):
	id_dict[item] = i
	i += 1

i = 0
newId1 = []
newId1_t = []
while i < len(data[0]):
	newId1.append(id_dict[data[0][i]])
	newId1_t.append(id_dict[data[1][i]])
	i += 1
print("finished id1")

filename = "2012Week/2012-"

file1 = open(filename+"01", 'w')
file2 = open(filename+"02", 'w')
file3 = open(filename+"03", 'w')
file4 = open(filename+"04", 'w')
file5 = open(filename+"05", 'w')
file6 = open(filename+"06", 'w')
file7 = open(filename+"07", 'w')
file8 = open(filename+"08", 'w')
file9 = open(filename+"09", 'w')
file10 = open(filename+"10", 'w')
file11 = open(filename+"11", 'w')
file12 = open(filename+"12", 'w')

j = 0
for item in data[2]:
	date = item.split("-")
	temp = [str(newId1[j]), str(newId1_t[j]), str(data[3][j]), str(data[4][j]), str(data[5][j]), str(data[6][j]), str(data[7][j]), str(data[8][j])]
	temp.extend([str(data[9][j]), str(data[10][j]), str(data[11][j]), str(data[12][j]), str(data[13][j]), str(data[14][j]), str(data[15][j]), str(data[16][j]), str(data[17][j])])
	
	if date[1] == "01":
		file1.write(','.join(temp))
		file1.write("\n")
	if date[1] == "02":
		file2.write(','.join(temp))
		file2.write("\n")
	if date[1] == "03":
		file3.write(','.join(temp))
		file3.write("\n")
	if date[1] == "04":
		file4.write(','.join(temp))
		file4.write("\n")
	if date[1] == "05":
		file5.write(','.join(temp))
		file5.write("\n")
	if date[1] == "06":
		file6.write(','.join(temp))
		file6.write("\n")
	if date[1] == "07":
		file7.write(','.join(temp))
		file7.write("\n")
	if date[1] == "08":
		file8.write(','.join(temp))
		file8.write("\n")
	if date[1] == "09":
		file9.write(','.join(temp))
		file9.write("\n")
	if date[1] == "10":
		file10.write(','.join(temp))
		file10.write("\n")
	if date[1] == "11":
		file11.write(','.join(temp))
		file11.write("\n")
	if date[1] == "12":
		file12.write(','.join(temp))
		file12.write("\n")
	j += 1

### if want the original date as input
'''
j = 0
for item in data[2]:
	date = item.split("-")
	temp = [str(newId1[j]), str(newId1_t[j]), str(data[2][j]), str(data[3][j]), str(data[4][j]), str(data[5][j]), str(data[6][j]), str(data[7][j]), str(data[8][j])]
	temp.extend([str(data[9][j]), str(data[10][j]), str(data[11][j]), str(data[12][j]), str(data[13][j]), str(data[14][j]), str(data[15][j]), str(data[16][j]), str(data[17][j])])
	
	if date[1] == "01":
		file1.write(','.join(temp))
		file1.write("\n")
	if date[1] == "02":
		file2.write(','.join(temp))
		file2.write("\n")
	if date[1] == "03":
		file3.write(','.join(temp))
		file3.write("\n")
	if date[1] == "04":
		file4.write(','.join(temp))
		file4.write("\n")
	if date[1] == "05":
		file5.write(','.join(temp))
		file5.write("\n")
	if date[1] == "06":
		file6.write(','.join(temp))
		file6.write("\n")
	if date[1] == "07":
		file7.write(','.join(temp))
		file7.write("\n")
	if date[1] == "08":
		file8.write(','.join(temp))
		file8.write("\n")
	if date[1] == "09":
		file9.write(','.join(temp))
		file9.write("\n")
	if date[1] == "10":
		file10.write(','.join(temp))
		file10.write("\n")
	if date[1] == "11":
		file11.write(','.join(temp))
		file11.write("\n")
	if date[1] == "12":
		file12.write(','.join(temp))
		file12.write("\n")
	j += 1

'''






