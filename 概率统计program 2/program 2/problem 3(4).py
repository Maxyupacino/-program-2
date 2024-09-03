import numpy as np


def simulate_stock_price(n, simulations):
    # 初始化价格为 100 元
    prices = np.full(simulations, 100.0)

    # 模拟每一天的价格变化
    for _ in range(n):
        # 生成随机涨跌因子
        factors = np.random.choice([1.7, 0.5], size=simulations)
        # 更新价格
        prices *= factors

    # 计算平均价格
    average_price = np.mean(prices)
    return average_price


# 理论值
def theoretical_average_price(n):
    return 100 * (1.1 ** n)


# 模拟参数
simulations = 100000000
ns = [1, 10, 30, 60]

# 计算模拟值并打印结果
for n in ns:
    simulated_average_price = simulate_stock_price(n, simulations)
    theoretical = theoretical_average_price(n)
    print(f"n={n}: 模拟平均价格={simulated_average_price:.2f}, 理论值={theoretical:.2f}")