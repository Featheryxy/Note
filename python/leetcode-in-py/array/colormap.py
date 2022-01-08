l = 1
r = x // 2
while l <= r:
	mid = (l+r) // 2
	if mid**2 <= x and（mid+1)**2 >= x:
		return mid
	if mid**2 <= x and （mid+1)**2 <= x:
		l = mid + 1
	else:
		r = mid - 1

