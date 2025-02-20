Tuples = {} # Ordered and unchangeable,Duplicates ok, Faster

fruits = ("Apple","Orange","Banana")

print(dir(fruits)) # to check methods available
print(help(fruits)) # for help of this collection
print(len(fruits)) # check out the length of the collection
print("Apple" in fruits) # check whether this exist in out collection

# def caesar_bruteforce(ciphertext):
#     for shift in range(1, 26):  # Shift from 1 to 25
#         decrypted = ''
#         for char in ciphertext:
#             if char.isalpha():
#                 base = ord('A') if char.isupper() else ord('a')
#                 decrypted += chr((ord(char) - base - shift) % 26 + base)
#             else:
#                 decrypted += char
#         print(f"Shift {shift}: {decrypted}")

# ciphertext = "q{vpln'bH_varHuebcrqxetrHOXEj"
# caesar_bruteforce(ciphertext)



