def palindrome():
    x=input("enter string: ")
    y=x[::-1]
    return y==x
print(palindrome())
