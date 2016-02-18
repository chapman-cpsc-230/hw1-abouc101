x=1
while x>0:
    Seconds = input ('Please enter any amount of seconds')
    Y=Seconds/60.0000/60/24/365
    if Y>100:
        print "No the baby won't live"
    else:
        print "Yes the baby will live"
    print "There are %d years in %d Seconds" % (Y, Seconds)
    name = input ('')
