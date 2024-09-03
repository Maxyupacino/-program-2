import numpy as np
import matplotlib.pyplot as plt

# 模拟时间长度（秒）
simulation_time = 10 * 3600

# 模拟参数
lambda_1 = 100  # 光电管1的暗电流事例率 (Hz)
lambda_2 = 200  # 光电管2的暗电流事例率 (Hz)
tau = 10e-6     # 事件A的时间差阈值 (秒)

# 生成光电管事件序列
def generate_events(lambda_, simulation_time):
    time = 0
    events = []
    while time < simulation_time:
        time += np.random.exponential(1 / lambda_)
        events.append(time)
    return np.array(events)

# 计算事件A的时间差
def calculate_event_time_differences(events_1, events_2, tau):
    # 对事件列表进行排序
    events_1_sorted = np.sort(events_1)
    events_2_sorted = np.sort(events_2)

    event_times = []
    i = 0  # 光电管1事件索引
    j = 0  # 光电管2事件索引

    while i < len(events_1_sorted) and j < len(events_2_sorted):
        time_diff = np.abs(events_1_sorted[i] - events_2_sorted[j])
        if time_diff < tau:
            event_times.append(min(events_1_sorted[i], events_2_sorted[j]))

        # 移动指针
        if events_1_sorted[i] < events_2_sorted[j]:
            i += 1
        else:
            j += 1

    return np.array(event_times)

# 模拟产生事件序列
events_1 = generate_events(lambda_1, simulation_time)
events_2 = generate_events(lambda_2, simulation_time)
print(events_1)
print(events_2)

# 模拟计算事件1的时间差
delta = []
for i in range(len(events_1)-1):
    delta_i = events_1[i+1] - events_1[i]
    delta.append(delta_i)

# 以0.005s为时间间隔计算次数
number_1 = []
for i in range(20):
    count = 0
    for j in range(len(delta)):
        if i * 0.005 < delta[j] < (i+1) * 0.005 :
            count += 1
    number_1.append(count)
time_1 = [i * 0.005 for i in range(20)]

# 画出number_1的直方分布图
plt.bar(time_1, number_1 , width = 0.0045, color = 'blue', label = 'num')
plt.xlabel('time/s')
plt.ylabel('number')
plt.grid(True)
plt.legend()
plt.show()

# 计算事件A的时间差
event_times_A = calculate_event_time_differences(events_1, events_2, tau)
print(event_times_A)

# 再计算相对时间差
diff = []
for i in range(len(event_times_A)-1):
    diff_i = event_times_A[i+1] - event_times_A[i]
    diff.append(diff_i)

# 以0.5s为时间间隔计算次数
number_2 = []
for i in range(40):
    count = 0
    for j in range(len(diff)):
        if i * 0.5 < diff[j] < (i+1) * 0.5 :
            count += 1
    number_2.append(count)
time_2 = [i * 0.5 for i in range(40)]

# 绘制直方图
plt.bar(time_2, number_2,  width = 0.45, color = 'blue', label = 'num')
plt.xlabel('Time Difference (s)')
plt.ylabel('Probability Density')
plt.title('Distribution of Time Differences between Consecutive Event A')
plt.show()

# 统计事件A的数量
num_events_A = len(event_times_A)
print("Number of events A found:", num_events_A)

# 估计事件A的事例率
lambda_A = num_events_A / simulation_time
print("Estimated rate of events A:", lambda_A)
