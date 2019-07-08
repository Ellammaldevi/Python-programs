# "D" for deposit, "W" for withdrawal 

import sys
netAmount = 0
while True:
    s = input("Enter transaction:")
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass

    string = input ("want to continue (Y for yes) : ")


print ("NetAmount: ",netAmount)