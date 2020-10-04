def getTotalBudget(people):
    ans = 0
    for person in people:
        ans += person["budget"]

    return ans
