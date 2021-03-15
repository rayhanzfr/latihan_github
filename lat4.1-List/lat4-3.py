result_str = ""

for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    

print(result_str)

result_str=""    
for row in range(0,7):    
    for column in range(0,7):     
        if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)

# for i in range(0,a,1) :
#     for j in range(0,a,1) :
#         if i==0 or i==a-1 or j==0 or j==a-1 :
#             print (end=" * ")
#         else :
#             print(end="   ")
#     print (" ")