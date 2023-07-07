def maximumWealth(accounts):
    money = 0
    for i in accounts:
        money = max(money, sum(i))
    
    return money

print(maximumWealth([[1,2,3],[3,2,1]]))