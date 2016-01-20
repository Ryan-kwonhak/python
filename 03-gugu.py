
def gugu(i):
    for j in range (2, 10) :
        print '{0} * {1} = %s'.format(i,j) %(int(i)*j)
i=raw_input("Input Number : ")
def mod(i):
    if int(i)%2 :
        print "It's ODD"
    else :
        print "It's EVEN"
gugu(i)
mod(i)
