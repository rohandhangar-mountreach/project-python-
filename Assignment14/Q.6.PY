# Q6
arr = np.random.randint(1,101,(5,5))
print(arr)
print("Diagonal:", np.diag(arr))
print("Greater than 50:", arr[arr>50])
arr[arr<30] = 0
print(arr)