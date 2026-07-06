# Q5
arr = np.array([[10,20,30,40],
                [50,60,70,80],
                [90,100,110,120]])

print("First Row:", arr[0])
print("Last Column:", arr[:,-1])
print("Center 2x2:\n", arr[1:3,1:3])
print("Even Numbers:", arr[arr%2==0])