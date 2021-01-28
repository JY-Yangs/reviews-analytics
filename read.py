data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 # 就是count = count + 1
		if count % 1000 == 0: # 這樣可以每數1000才印一次, 可增加速度
		# 如果"count"跟"1000"的"餘數等於0"的意思
		# "%"就是求餘數的運算符號, ex: 1003 % 1000 = 3 ; 10 % 6 = 4 
			print(count) # 這裡印出來可以看出讀的進度到哪了
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) # 就是sum_len = sum_len + len(d)
print('留言的平均長度是', sum_len/len(data))



new = []
for d in data: # 把data這個清單裡面的東西一筆一筆的叫出來
	if len(d) < 100:
		new.append(d) # 如果d長度<100, 就把它裝進"new這個清單裡面"
print('一共有', len(new), '筆留言長度小於100') # 可以看出"new這個清單"裡面有幾筆資料
print(new[0])
print(new[1])

