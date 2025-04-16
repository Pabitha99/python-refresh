# 1.Write a Python function that takes a string and returns it reversed.
# Input: "hello"
# Output: "olleh"
Input_val="hello"
Output_val=Input_val[::-1]
print(Output_val)

# 2.Write a function to check if a string is a palindrome (reads the same forwards and backwards).
# Input: "madam"
# Output: True
Input_val="madam"
Output_val=Input_val[::-1]
if Input_val==Output_val:
    print("it is palindrome")
else:
    print("it is not palindrome")

# 3.Count how many vowels (a, e, i, o, u) are in a given string.
# Input: "Babida"
# Output: 3
Input_val="Babida"
vowels=['a','e','i','o','u']
count=0
for i in Input_val:
    if i in vowels:
        count=count+1
print(count)

# 4.Write a function to find the maximum number in a list without using Python’s built-in max() function.
# Input: [2, 5, 1, 9, 3]
# Output: 9
Input_val=[2, 5, 1, 9, 3]
max_val=Input_val[0]
for i in Input_val:
    if i>max_val:
        max_val=i
print(max_val)
# 5. FizzBuzz (Classic)
# Print numbers from 1 to 20. But:

# If the number is divisible by 3, print "Fizz"

# If divisible by 5, print "Buzz"

# If divisible by both, print "FizzBuzz"

for i in range(1,21):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    