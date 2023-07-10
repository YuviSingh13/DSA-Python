def maxProfit(prices):
    profit = 0
    cost = 999999
    for i in range(len(prices)):
        cost = min(cost, prices[i])
        profit = max(prices[i] - cost, profit)
    print("Profit : ", profit)



priceList = [7, 1, 5, 3, 6, 4]
maxProfit(priceList)