n=[44,58,94,89,99,356,956,111]
def find_length(n):
	length=len(n)
	n.sort()
	print("Largest number is :", n[length-1])
	print("Largest number is :", n[length-2])
find_length(n)
