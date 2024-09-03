import random
import matplotlib.pyplot as plt

number = 1000000
countnumber = 0
station = [0,0,0,0,0,0,0,0,0,0]
# 随机模拟20次
for k in range(number):
    c = []
    for i in range(20):
        c_i = random.randint(1,10)
        c.append(c_i)

    count = []
    #计数
    for j in range(len(c)):
        if c[j] in count:
            continue
        else:
            count.append(c[j])

    count1 = len(count)
    countnumber += count1
    station[count1 - 1] += 1

print(countnumber)

# 计算平均值
avragecount = countnumber / number
print('站数的平均值：',avragecount)

plt.bar(range(1,11), station,  width = 0.95, color = 'blue', label = 'num')
plt.xlabel('station')
plt.ylabel('number')
plt.title('station-number')
plt.show()

