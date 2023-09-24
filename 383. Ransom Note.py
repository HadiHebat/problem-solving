s = 'aa'
t= 'aab'
x = [i for i in t] 
print (x)
res = any(ele in s for ele in x)
print(str(res))