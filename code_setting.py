password = 'a123456'
time = 3
print('最多輸入3次密碼')

while True:
	guess = input('請輸入密碼: ', )

	if guess == password:
		print('登入成功')
		break
	else:
		time = time - 1
		if time > 0:
			print('密碼錯誤, ''您還剩', time, '次機會')

		else:
			print('密碼錯誤, 輸入次數已達上限')
			break