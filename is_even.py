#Create a variable "number" and assign it a integer value.

#Print 1 if the number is even, otherwise print 0.
number = int(input("Hoxlagan son kiriting\nmen sizga toq yoki juft ekalnigini aytaman"))
answer = (number%2)
if answer == 0:
    print(f"Kiritgan soniz juft {number}")
else:
    print(f"Kiritgan soniz toq {number}")