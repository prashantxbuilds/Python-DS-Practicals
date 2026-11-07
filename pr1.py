
books = ["Python", "Java", "C++", "DBMS", "OS"]
borrow = [5, 3, 0, 7, 5]

# A. Average borrowing
avg = sum(borrow) / len(borrow)
print("Average Borrowing:", avg)

# B. Highest and Lowest borrowing
print("Highest Borrowing:", max(borrow))
print("Lowest Borrowing:", min(borrow))

# C. Members with zero borrowing
print("Zero Borrowing Members:", borrow.count(0))

# D. Mode of borrowing
mode = max(set(borrow), key=borrow.count)
print("Most Frequent Borrowing:", mode)
