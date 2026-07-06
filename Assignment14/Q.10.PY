# Q10
marks = np.random.randint(30,101,(10,5))

print(marks)

total = marks.sum(axis=1)
avg = marks.mean(axis=1)

print("Total:", total)
print("Average:", avg)

print("Highest Student:", total.argmax())
print("Lowest Student:", total.argmin())

print("Class Mean:", marks.mean())
print("Class Std:", marks.std())

top3 = np.argsort(total)[-3:]
print("Top 3 Students Marks:")
print(marks[top3])