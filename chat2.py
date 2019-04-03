def read_file(filename):
	lines = []
	with open(filename, 'r', encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip()) #strip移除句尾換行符號
	return lines

def count(lines):
	person = None #預設值是虛無
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ') #split遇到空格就切割句子
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allens total word count', allen_word_count)
	print('allens sticker count', allen_sticker_count)
	print('allens image count', allen_image_count)
	print('vikis total word count', viki_word_count)
	print('vikis sticker count', viki_sticker_count)
	print('vikis image count', viki_image_count)
		

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('-LINE-Viki.txt') #使用function時才投入檔名
	lines = count(lines) #把lines投入convert function
	#write_file('output.txt', lines)

main()