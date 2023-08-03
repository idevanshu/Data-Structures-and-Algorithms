def numberOfEmployeesWhoMetTarget(hours,target):
    count = 0
    for i in hours:
        if i >= target:
            count += 1
        return count