#Auto List Generator

import random

L = []

N = "0123456789"

print("How many elements N must the list contain?")
A = eval(input("Input: "))

print("How many digits must an element N have?")
B = eval(input("Input: "))

for i in range(A):
    length = B
    O = "".join(random.sample(N, length))
    L.append(O)
print(f"Your generated list is: {L} ")


print("--------------------")
print("")
print("Code made by 𝕱𝖆𝖇𝖎𝖓𝖍𝖔")
print("")