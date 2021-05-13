n1=input("n1:")
n2=input("n2:")
n1=int(n1,5)
n2=int(n2,5)

print("n1=",bin(n1))
print("n2=",bin(n2))

bit_or=n1| n2
bit_and=n1 & n2
bit_xor=n1^n2

bit_or=bin(bit_or)
bit_and=bin(bit_and)
bit_xor=bin(bit_xor)

print("n1=",bin(n1))
print("n2=",bin(n2))
print("or=",bit_or)
print("and=",bit_and)
print("xor=",bit_xor)
