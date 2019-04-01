def read_file(filename):
	lines = []
	with open(filename, 'r', encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None #預設值是虛無
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue #如果是Allen，跳過Allen人名這一行，才改成對話
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有值的話才執行
			new.append(person + ": " + line) #那一行不是Allen也不是Tom才改成對話紀錄
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt') #使用function時才投入檔名
	lines = convert(lines) #把lines投入convert function
	write_file('output.txt', lines)

main()