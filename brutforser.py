from vizhiner import * 

print("Введите закрытый текст:")
text = input()
print("Введите тип шифра:\n 1 - самоключ;\n 2 - самоключ по шифротексту.")
type = int(input())

for key in "qwertyuiopasdfghjklzxcvbnm":
	open_text = decrypt(text, key, type+1)
	print(key,'-',open_text[:40])