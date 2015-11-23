import sys, random

fromThis = sys.argv[2]
toThat = sys.argv[3]

f = open(sys.argv[1], "r")

eng_to_obj = {}
pinyin_to_obj = {}
char_to_obj = {}
trad_to_obj = {}
simp_to_obj = {}

ENGLISH = 0
PINYIN = 1
TRAD = 2
SIMP = 3
CHAR = 4

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

input_to_result = {
	"eng": ENGLISH,
	"pinyin": PINYIN,
	"trad": TRAD,
	"simp": SIMP,
	"char": CHAR
}

def green_check():
	return bcolors.OKGREEN + '\u2713' + bcolors.ENDC

def red_x():
	return bcolors.FAIL + '\u2717' + bcolors.ENDC



if fromThis not in input_to_result or toThat not in input_to_result:
	raise("You input the following:", fromThis, toThat, "Try Again.")
from_enum_val = input_to_result[fromThis]
to_enum_val = input_to_result[toThat]

# print(from_enum_val, to_enum_val)

class Chinese:
	def __init__(self, english, pinyin, trad, simp):
		self.english = english
		self.pinyin = pinyin
		self.trad = trad
		self.simp = simp

	def details(self):
		return self.english, self.pinyin, self.trad, self.simp

	def get_item(self, enum_val):
		if enum_val == ENGLISH:
			return self.english
		elif enum_val == PINYIN:
			return self.pinyin
		elif enum_val == TRAD:
			return self.trad
		elif enum_val == SIMP:
			return self.simp

while True:
	english = f.readline().strip()
	if not english: break
	pinyin = f.readline().strip()
	if not pinyin: break
	trad = f.readline().strip()
	if not trad: break
	simp = f.readline().strip()
	if not simp: break
	new_chinese_obj = Chinese(english, pinyin, trad, simp)
	eng_to_obj[english] = new_chinese_obj
	pinyin_to_obj[pinyin] = new_chinese_obj
	char_to_obj[trad] = new_chinese_obj
	trad_to_obj[trad] = new_chinese_obj
	if "-" not in simp:
		char_to_obj[simp] = new_chinese_obj
		simp_to_obj[simp] = new_chinese_obj

# for char in chinese_list:
# 	print(char.english, char.pinyin, char.trad, char.simp)

def unload(problems_left, incorrect, object_dict, num_problems, enum_val):
	# print("Enters unload")
	problems_so_far = num_problems
	while len(problems_left) > 0:
		key = problems_left[0]
		result = object_dict[key].get_item(enum_val)

		if enum_val == ENGLISH:
			guess = input("Guess for " + key + ": ")
			if guess.strip() == "":
				obj = object_dict[key]
				print(red_x(), "WRONG!", obj.english, "==", obj.pinyin, "==", obj.trad)
				incorrect.append(key)
				problems_left.append(key)
				problems_so_far += 1
			elif guess in result.split():
				print(green_check(), "CORRECT!", key, "==", result)
			elif guess in result:
				print(green_check(), "CORRECT!", key, "==", result)
			else:
				obj = object_dict[key]
				print(red_x(), "WRONG!", obj.english, "==", obj.pinyin, "==", obj.trad)
				incorrect.append(key)
				problems_left.append(key)
				problems_so_far += 1

		elif enum_val == PINYIN:
			guess = input("Guess for " + key + ": ")
			if guess == result:
				print(green_check(), "CORRECT!", key, "==", result)
			else:
				obj = object_dict[key]
				print(red_x(), "WRONG!", obj.pinyin, "==", obj.trad, "==", obj.english)
				incorrect.append(key)
				problems_left.append(key)
				problems_so_far += 1
		elif enum_val == TRAD:
			guess = input("Guess for " + key + "(Press Enter):")
			print(result, "<-- Answer")
			correctResult = True if input("Did you get it right? y/n?") == "y" else False
			if correctResult:
				print(green_check(), "CORRECT! Nice!")
			else:
				obj = object_dict[key]
				print(red_x(), "WRONG!", obj.trad, "==", obj.pinyin, "==", obj.english)
				incorrect.append(key)
				problems_left.append(key)
				problems_so_far += 1

		del problems_left[0]
	return problems_so_far

def solve(keys, object_dict, enum_val):
	# print("Enters solve")
	random.shuffle(keys)
	problems_left = keys
	num_problems = len(keys)
	incorrect = []
	problems_solved = unload(problems_left, incorrect, object_dict, num_problems, enum_val)

	print("Here's the ones you got wrong!")
	for key in incorrect:
		print(key, "--", object_dict[key].get_item(enum_val))
	correct_num = problems_solved - len(incorrect)
	print("ACCURACY:", correct_num, "/", problems_solved, ":", int(100 * correct_num/problems_solved), "%")

def obj_details(chinese_obj):
	return chinese_obj.details()

def eng_to_pinyin():
	eng_keys = list(eng_to_obj.keys())
	solve(eng_keys, eng_to_obj, PINYIN)

def pinyin_to_char():
	pinyin_keys = list(pinyin_to_obj.keys())
	solve(pinyin_keys, pinyin_to_obj, TRAD)

def pinyin_to_eng():
	pinyin_keys = list(pinyin_to_obj.keys())
	solve(pinyin_keys, pinyin_to_obj, ENGLISH)

def char_to_pinyin():
	char_keys = list(char_to_obj.keys())
	solve(char_keys, char_to_obj, PINYIN)

def char_to_eng():
	char_keys = list(char_to_obj.keys())
	solve(char_keys, char_to_obj, ENGLISH)

def simp_to_eng():
	simp_keys = list(simp_to_obj.keys())
	solve(simp_keys, simp_to_obj, ENGLISH)

def trad_to_eng():
	trad_keys = list(trad_to_obj.keys())
	solve(trad_keys, trad_to_obj, ENGLISH)

def eng_to_trad():
	eng_keys = list(eng_to_obj.keys())
	solve(eng_keys, eng_to_obj, TRAD)

if from_enum_val == ENGLISH and to_enum_val == PINYIN:
	eng_to_pinyin()
elif from_enum_val == PINYIN and to_enum_val == CHAR:
	pinyin_to_char()
elif from_enum_val == PINYIN and to_enum_val == ENGLISH:
	pinyin_to_eng()
elif from_enum_val == CHAR and to_enum_val == PINYIN:
	char_to_pinyin()
elif from_enum_val == SIMP and to_enum_val == ENGLISH:
	simp_to_eng()
elif from_enum_val == TRAD and to_enum_val == ENGLISH:
	trad_to_eng()
elif from_enum_val == ENGLISH and to_enum_val == TRAD:
	eng_to_trad()
elif from_enum_val == CHAR and to_enum_val == ENGLISH:
	char_to_eng()