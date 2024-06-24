# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.    

    #Enter Python code here and hit the Run button.

def calc (num1,num2):
    product = num1*num2
    sum = num1 + num2
    if product<=1000:
        return product
    else:
        return sum
        
result = calc(100,30)
print("The result is", result)
