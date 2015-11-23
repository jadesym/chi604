import sys, random
chapter_num  = sys.argv[1]
f = open(chapter_num, "r")

engToPinyin = {}

while True:
	english = f.readline().strip()
	pinyin = f.readline().strip()
	if not pinyin: break
	engToPinyin[english] = pinyin


incorrect = []
english_keys = list(engToPinyin.keys())
random.shuffle(english_keys)
problems_left = english_keys

additional = 0
while len(problems_left) > 0:
	key = problems_left[0]
	pinyin = engToPinyin[key]
	english = key
	# result = chinese_character.encode('big5').decode('big5')
	guess = input("Guess for - " + english + ": ")
	if guess == pinyin:
		print("CORRECT!", english, "==", pinyin)
	else:
		print("WRONG!", english,"==", pinyin)
		incorrect.append(english)
		problems_left.append(english)
		additional += 1
	del problems_left[0]

print("Here's the ones you got wrong!")
for key in incorrect:
	print(key, "--", engToPinyin[key])
correct_num = len(engToPinyin) + additional - len(incorrect)
print("ACCURACY:", correct_num, "/", len(engToPinyin) + additional, ":", int(100 * correct_num/(len(engToPinyin) + additional)), "%")
