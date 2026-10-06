salary1 = [4000,3000,1000,2000]
salary2 = [1000,2000,3000]

# ACCEPTED
def sol(salary):
    salary.sort()
    salary.pop(0)
    salary.pop(-1)

    return sum(salary) / len(salary)

# ALTERNATIVE
def sol(salary):
    total = sum(salary)
    minn = min(salary)
    maxx = max(salary)
    
    return (total - minn - maxx) / (len(salary) - 2)

print(sol(salary1))
print(sol(salary2))