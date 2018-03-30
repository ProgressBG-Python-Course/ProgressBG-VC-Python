first_names  = ("ivan" ,"maria" , "prtar")
sur_name = ("ivanov" , "popova" , "petrov")
# iep: discuss
# names = first_names[0], sur_name[0] ,
# 				first_names[1] ,sur_name[1] ,
# 				first_names[2], sur_name[2]

names = []
for i in range(len(first_names)):
	# names.append(first_names[i], sur_name[i])
	names = names + [first_names[i]] + [sur_name[i]]

print(names)
