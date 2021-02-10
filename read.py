import time # python內建的標準函式庫本身就有time()這個module
import progressbar # 由網路上下載下來的module ( PYPI: The Python Package Index)

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
# 使用方法可以到PYPI裡面的這個套件看說明, Note: ProgressBar(max_value=1000000)這是一個這一個發明者發明的"物件", 這"不是function", 因為他字母開頭字大寫, function開頭一定是小寫 (行內的規局, 大家都會照這樣的規局寫)
# ProgressBar()是一個"物件", 他的data type是: ProgressBar(作者寫的)
# 要寫"class"才能夠自行發行"資料型別(data type)"
# python內建data type: int, flaot, bool, str, list, dict
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count) # function的第一個字母一定是小寫的, ex: "update()"這個就是function
print('檔案讀取完了, 總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度是', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')

# 文字計數
start_time = time.time() # 使用time這個模組裡面"的"time這個function, 紀錄此刻的時間
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
end_time = time.time() # 紀錄此刻的時間
print('花了', end_time - start_time, '秒')

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