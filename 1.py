name = input('введите имя: ')
fam = input('введите фамилию: ')
years = int(input('введите возраст: '))
massa = int(input('введите вес: '))

if years <= 30 and 50 <= massa <= 120:
	print(name, fam, years,'год, вес', massa, ' - хорошее состояние')
elif years > 30 and (massa < 50 or massa > 120):
	print(name, fam, years,'год, вес', massa,' - требуется начать правильный образ жизни')
elif years > 40 and (massa < 50 or massa > 120):
	print(name, fam, years,'год, вес', massa, ' - обратитесь к врачу')
else : print('До свидания!')