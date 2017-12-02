import pandas as pd 


'''
data1 = pd.read_csv("split_2012", header=None)
data2 = pd.read_csv("split_2013", header=None)
data3 = pd.read_csv("split_2014", header=None)
data4 = pd.read_csv("split_2015", header=None)
data5 = pd.read_csv("split_2016", header=None)

id_dict = {}
id1_f = list(set(data1[0]))
id1_t = list(set(data1[1]))
id2_f = list(set(data2[0]))
id2_t = list(set(data2[1]))
id3_f = list(set(data3[0]))
id3_t = list(set(data3[1]))
id4_f = list(set(data4[0]))
id4_t = list(set(data4[1]))
id5_f = list(set(data5[0]))
id5_t = list(set(data5[1]))
temp = [id1_f, id1_t, id2_f, id2_t, id3_f, id3_t, id4_f, id4_t]
id_set = set().union(*temp)

i = 1
for item in list(id_set):
	id_dict[item] = i
	i += 1
'''

# print(node)

## file structure changed!!
## file structure changed!!
## file structure changed!!
## file structure changed!!


j = 1
while j <= 12:
	print(j)
	filename = "ByMonthNoWeek/2016/2016-"
	if j < 10:
		filename += "0" + str(j)
	else:
		filename += str(j)

	data = pd.read_csv(filename, header=None)
	node = {}
	print("finish reading")

	i = 0
	while i < len(data[0]):
		if data[0][i] not in node:
			node[data[0][i]] = {}
		if data[1][i] not in node[data[0][i]]:
			node[data[0][i]][data[1][i]] = [data[2][i], data[3][i]+data[2][i]]
		else:
			node[data[0][i]][data[1][i]][0] += data[2][i]
			node[data[0][i]][data[1][i]][1] += data[2][i]+data[3][i]
		i += 1

	i = 0
	while i < len(data[1]):
		if data[1][i] not in node:
			node[data[1][i]] = {}
		if data[0][i] not in node[data[1][i]]:
			node[data[1][i]][data[0][i]] = [data[7][i], data[7][i]+data[8][i]]
		else:
			node[data[1][i]][data[0][i]][0] += data[7][i]
			node[data[1][i]][data[0][i]][1] += data[7][i]+data[8][i]
		i += 1

	print("finish create nodes")

	filename = "ByMonthNoWeek/2016/ask_send/2016-"
	if j < 10:
		filename += "0" + str(j)
	else:
		filename += str(j)

	file = open(filename+"-type3", 'w')
	for id1 in node.keys():
		for id2 in node[id1].keys():
			if node[id1][id2][0] != 0 and node[id1][id2][1] != 0:
				file.write(str(id1) + "," + str(id2) + "," + str(float(node[id1][id2][0]) / node[id1][id2][1])+ "\n")
			elif node[id1][id2][0] == 0 and node[id1][id2][1] != 0:
				file.write(str(id1) + "," + str(id2) + "," + str(0.0001 / node[id1][id2][1]) + "\n")
	print("finish writing to file")

	j += 1

