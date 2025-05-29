# palindrome

def palin(text):
    if len(text) <=1:
        print("this is a palindrome")
    else:
        if text[0] == text[-1]: 
            palin(text[1:-1])
        else:
            print("this is not a palindrome")