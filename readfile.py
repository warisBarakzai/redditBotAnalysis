

file = open('GI_assets_publicMap_construct.csv')
returnList = []
lst = file.readlines()
for i in lst:
	i.strip('\n')
	pew = i.split(',')
	for k in range(len(pew[1])):
		if (pew[1][k:k+10] == 'Green Roof'):
			returnList.append(pew)

for i in returnList:
	print(i[1])