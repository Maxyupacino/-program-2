import numpy as np
import matplotlib.pyplot as plt


def simulate_stock_price(n, simulations):
    # 初始化价格为 100 元
    prices = np.full(simulations, 100.0)

    # 模拟每一天的价格变化
    for _ in range(n):
        # 生成随机涨跌因子
        factors = np.random.choice([1.7, 0.5], size=simulations)
        # 更新价格
        prices *= factors

    # 计算小于 1 的价格数量
    count_less_than_1 = np.sum(prices < 1)
    # 计算概率
    probability = count_less_than_1 / simulations
    return probability


# 模拟参数
simulations = 1000000
ns = [1, 10, 30, 60, 90, 180, 360]

# 计算概率并绘制图表
probabilities = []
for n in ns:
    probability = simulate_stock_price(n, simulations)
    probabilities.append(probability)

# 计算误差棒
error = np.sqrt(np.array(probabilities) * (1 - np.array(probabilities)) / simulations)

# 绘制图表
plt.errorbar(ns, probabilities, yerr=error, fmt='o', capsize=5)
plt.xlabel('n')
plt.ylabel('p')
plt.title('p vs n')
plt.grid(True)
plt.show()