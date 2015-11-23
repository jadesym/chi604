import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
for file_num in range(start, end + 1):
	file_num = str(file_num)
	engFile = open(file_num + ".eng", 'r')
	phraseFile = open(file_num + ".phrase", 'w')
	while True:
		english = engFile.readline()
		if not english:
			break
		pinyin = engFile.readline()
		if not pinyin:
			break
		phraseFile.write(pinyin)
