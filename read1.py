# 一百萬筆留言中最常出現那些字

data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(count)
print('檔案讀取完了, 總共有', len(data), '筆資料')

print(data[0])

wc = {} # word_count
for d in data:
	words = d.split() # split完後變清單 ; split()預設值為"切空白鍵", 且用預設值去切的話，遇到連續的"空白鍵"他就不會切成連續的"空字串"
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增key-value pair進"字典"

for word in wc: # word會是字典裡面的"每一個key", 這個for迴圈會把字典裡面的key"一個一個拿出來"
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')