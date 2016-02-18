print "Interest Rate Calculator!"
A = input ('Please Enter an Initial Amount')
P = input ('Please Enter Bank Interest Rate')
N = input ('Please Enter a number of years the bank will hold the money')
Final = (A * (1 + (float(P)/100))**N)
print Final, "Is how much money you will have at withdrawal"
name = input ('')
