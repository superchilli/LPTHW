# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
# 当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

def sensitiveWord(path):
	sensWord=[]
	with open(path) as f:
		for line in f.readlines():
			sensWord.append(line.strip())

	userInput = input('>: ')

	for i in sensWord:
		if i in userInput:
			userInput = userInput.replace(i, '**')
	print(userInput)


if __name__ == '__main__':
	sensitiveWord('filter.txt')

