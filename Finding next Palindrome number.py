# find the next palindrome number from the given number
# Define the function to find the next palindrome number

def next_palindrome(n):
    while True:
        m = int(str(n)[::-1])
        if m == n:
            return n
        else:
            n = n + 1

# Take input from the user
print("\n This is the program to find the next palindrome number to the given number\n")
given_number = [int(item) for item in input(" Enter all the your numbers here with space in between them:\n ").split()]
Palindrome_number = []
# Print output
for i in range(len(given_number)):
    print(f"Next Palindrome for {given_number[i]} is {next_palindrome(given_number[i])} ")
    Palindrome_number.append(next_palindrome(given_number[i]))
print(given_number)
print(Palindrome_number)
