# Q9
arr = np.random.randn(6,6)

print(arr.shape)
print(arr.size)
print(arr.dtype)

print(np.unravel_index(arr.argmax(), arr.shape))
print(np.unravel_index(arr.argmin(), arr.shape))

print(arr[:3,:3])

arr = np.abs(arr)
print(arr.mean())