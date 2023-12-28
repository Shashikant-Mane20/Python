input_tuple=(1,2,3,4,5)
list=[]
for x in reversed(input_tuple):
    list.append(x)
    
out_tuple=tuple(list)
print(out_tuple)