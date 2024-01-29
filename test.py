def prime_divisor(num):
    counter=0
    divisor=2
    unique_factors= set()
    while divisor<= num :
        if num%divisor == 0 and divisor not in unique_factors:
            unique_factors.add(divisor)
            counter+=1
            num=num/divisor
        else:
            divisor+=1
    return counter
        
    
user_numbers=[]
for i in range(10):
    num=int(input('enter numbers \n'))
    user_numbers.append(num)
    

max_number= None
max_count = 0
for num in user_numbers:
    factor_count= prime_divisor(num)
    if factor_count> max_count:
        max_count=factor_count
        max_number=num
    elif factor_count==max_count and num> max_number:
            max_number=num
            
print('The number with the most prime factors is %s with %d prime factors'%(max_number,max_count))
