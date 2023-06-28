email = input("Enter Your Email: ").strip()
print(type(email))
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} & domain is {domain}")

# arr[start:stop]         # items start through stop-1
# arr[start:]             # items start through the rest of the array
# arr[:stop]              # items from the beginning through stop-1
# arr[:]                  # a copy of the whole array
# arr[start:stop:step]    # start through not past stop, by step