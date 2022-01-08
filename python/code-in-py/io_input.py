def reverse(text):
    return  text[::-1]

def is_palindrome(text):#回文
    return  text == reverse(text)

something = input("Enter text:")#input()函数可以接受一个字符串作为参数，并将其展示给用户
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")