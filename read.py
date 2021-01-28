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
print(len(data))
print(data[0])
print('--------------------')
print(data[1])