age = input('請輸入年齡:')
age = int(age)
if age < 13:
	print(國小)
elif age >=13 and age < 18:
	print('國高中')
elif age >= 18 and age < 28:
	ptint('大學、碩博士')
else:
	print('社會人士')