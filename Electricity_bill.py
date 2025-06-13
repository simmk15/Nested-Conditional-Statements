units=float(input("Enter the number of units consumed="))
if units<50:
    bill=units*2.60+25
    print("The electricity bill is ",bill)
elif units>=50 and units<100:
    bill=units*3.25+35
    print("The electricity bill is ",bill)
elif units>=100 and units<=200:
   bill=units*5.26+45
   print("The electricity bill is ",bill)
else:
   bill=units*8.45+75
   print("The electricity bill is ",bill)