
salary = [25000.50, 18000.75, 32000.00, 15000.25, 28000.50]

print("Original Salaries:", salary)

for i in range(len(salary)):
    min = i

    for j in range(i + 1, len(salary)):
        if salary[j] < salary[min]:
            min = j

    salary[i], salary[min] = salary[min], salary[i]

print("Sorted Salaries:", salary)
