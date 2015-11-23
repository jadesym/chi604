import sys

character_dict = {}

f = open(sys.argv[1], 'r')
while True:
	pinyin = f.readline().strip()
	character = f.readline().strip()
	if not character: break
	character_dict[pinyin] = character
import time
fout = open(sys.argv[1][:-3] + "_guess_char.out", 'w')
fout.write("-----------------------------")
fout.write("\n")
import random

incorrect = []
pinyin_keys = list(character_dict.keys())
random.shuffle(pinyin_keys)
problems_left = pinyin_keys
additional = 0
while len(problems_left) > 0:
	key = problems_left[0]
	chinese_character = character_dict[key]
	pinyin = key
	# result = chinese_character.encode('big5').decode('big5')
	guess = input("Guess for " + pinyin + "(Press Enter): ")
	print(chinese_character, "<-- Answer")
	correctResult = True if input("Did you get it right? y/n?") == "y" else False
	if correctResult:
		print("CORRECT! Nice!")
	else:
		print("WRONG!", pinyin,"==", chinese_character)
		fout.write("WRONG! " +  pinyin + " == " + chinese_character)
		fout.write("\n")
		incorrect.append(pinyin)
		problems_left.append(pinyin)
		additional += 1
	del problems_left[0]

print("Here's the ones you got wrong!")
for key in incorrect:
	print(key, "--", character_dict[key])
	fout.write(key + "--" + character_dict[key])
correct_num = len(character_dict) + additional - len(incorrect)
print("ACCURACY:", correct_num, "/", len(character_dict) + additional, ":", int(100 * correct_num/(len(character_dict) + additional)), "%")
fout.write("ACCURACY: " + str(correct_num) + "/" + str(len(character_dict) + additional) + " : " +  str(100 * correct_num/(len(character_dict) + additional)) + "%")
fout.write("-----------------------------")