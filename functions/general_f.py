def greatest_number(num1, num2,num3):
    greatestNum = 0
    if num1 > num2:
       greatestNum = num1
    elif num2 > num3:
       greatestNum = num2
    else:
       greatestNum = num3     
    return greatestNum

# Example usage:
def greatest_num_arr(num):
   #  num=[12,33,1,5,3,6,7]
    greatNum = 0
    index=0
    for idx, n in enumerate(num):
       if(greatNum<n):
          greatNum=n
          index=idx
    return greatNum,index