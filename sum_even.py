#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".

number = 1234


a = ((number%10))
b = (((number//10)%10))
c = (((number//100)%10))
d = ((number//1000))



e = (((a+1)%2)*a)
f = (((b+1)%2)*b)
g = (((c+1)%2)*c)
h = (((d+1)%2)*d)



var_int = (e+f+g+h)
print(var_int)

# print(a)
# print(b)
# print(c)
# print(d)
