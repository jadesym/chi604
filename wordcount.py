import re
with open('script.txt') as f:
	count = 0
	currentCount = 0
	index = 1
	totalLines = 0
	for line in f:
		lineWithoutName = (line.strip())[line.index(":") + 1:]
		lineWithoutParens = re.sub(r'\([^)]*\)', '',lineWithoutName)
		currentCount = len(lineWithoutParens)
		count += currentCount
		lineNumber = 0
		remainder = currentCount % 20
		dividend = currentCount // 20
		if remainder:
			lineNumber = dividend + 1
		else:
			lineNumber = dividend
		totalLines += lineNumber
		print(index, currentCount, totalLines, lineWithoutParens)
		index += 1
	print("Word Count: ", count)
