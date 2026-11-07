
salary = [25000.50, 18000.75, 32000.00, 15000.25, 28000.50, 45000.00, 38000.00]

print("Original Salaries:", salary)

# Bubble Sort
for i in range(len(salary)):
    for j in range(len(salary) - i - 1):
        if salary[j] > salary[j + 1]:
            salary[j], salary[j + 1] = salary[j + 1], salary[j]

print("Sorted Salaries:", salary)

# Top Five Highest Salaries
print("Top Five Highest Salaries:")
for i in range(len(salary) - 1, len(salary) - 6, -1):
    print(salary[i])
