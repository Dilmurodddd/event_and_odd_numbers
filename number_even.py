#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
number = 8521
a = ((number%10))
b = (((number//10)%10))
c = (((number//100)%10))
d = ((number//1000))

f = (((((number%10))+1)%2)+((((number//10)%10))+1)%2)+(((((number//100)%10))+1)%2)+((((number//1000))+1)%2)




# print(f)



number1t = 9876
g = ((number1t%10))
h = (((number1t//10)%10))
i = (((number1t//100)%10))
j = ((number1t//1000))

k = (((g+1)%2)*g)
l = (((h+1)%2)*h)
m = (((i+1)%2)*i)
n = (((j+1)%2)*k)

print(g)

print(h)

print(i)

print(j)

print(k)

print(l)

print(m)

print(n)