def maxProfit(prices,fee):
    # Status represent buying or selling for stocks.
    status = -prices[0]
    profit = 0

    for i in range(1,len(prices)):
        print(status)
        status = max(status, profit - prices[i])
        profit = max(profit, status+prices[i] - fee)

    return profit

print(maxProfit(prices = [1,3,2,8,4,9], fee = 2))