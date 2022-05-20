def BalancedBrackets(Str):
    
    stack = []


    
    for char in Str:
        
        if char == '{' or char == '(' or char == '[':
            stack.append(char)
            print(stack,"dddddddddddddddddd")
        elif char == '}' or char == ')' or char == ']':
            if len(stack) == 0:
                return False
            top_element = stack.pop()
            print(top_element,"ffffffffffffffffff")
            if not Compare(top_element, char):
                return False
      
    if len(stack) != 0:
        return False
              
    return True

 
def Compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True  
    return False

s=input("enter a string brackets:  ")
print("given string brackets is balanced or not: ",BalancedBrackets(s))


