import sys

character_dict = {}
extra_dict = {}
f = open(sys.argv[1], 'r')
for line in f:
	try:
		pinyin, character = line.split()
		character_dict[character] = pinyin
	except ValueError as e:
		pinyin, character, extra = line.split()
		character_dict[character] = pinyin
		extra_dict[character] = extra
import time
fout = open(sys.argv[1][:-2] + "out", 'w')
fout.write("-----------------------------")
fout.write("\n")
import random

incorrect = []
character_dict_keys = list(character_dict.keys())
random.shuffle(character_dict_keys)
problems_left = character_dict_keys
additional = 0
while len(problems_left) > 0:
	key = problems_left[0]
	pinyin = character_dict[key]
	chinese_character = key
	# result = chinese_character.encode('big5').decode('big5')
	guess = input("Guess for " + chinese_character + ": ")
	if guess == pinyin:
		print("CORRECT!", chinese_character, "==", pinyin)
	else:
		if chinese_character in extra_dict:
			print("WRONG!", chinese_character, extra_dict[chinese_character],"==", pinyin)		
		else:
			print("WRONG!", chinese_character,"==", pinyin)
		fout.write("WRONG! " + chinese_character + " == " + pinyin)
		fout.write("\n")
		incorrect.append(chinese_character)
		problems_left.append(chinese_character)
		additional += 1
	del problems_left[0]

print("Here's the ones you got wrong!")
for key in incorrect:
	print(key, "--", character_dict[key])
	fout.write(key + " -- " + character_dict[key])
correct_num = len(character_dict) + additional - len(incorrect)
print("ACCURACY:", correct_num, "/", len(character_dict) + additional, ":", int(100 * correct_num/(len(character_dict) + additional)), "%")
fout.write("ACCURACY: " + str(correct_num) + "/" + str(len(character_dict) + additional) + " : " + str(int(100 * correct_num/(len(character_dict) + additional))) + "%")
fout.write("-----------------------------")