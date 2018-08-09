
def sendToA ( P , G , Y ):
	print "In Alice"
	M = input("Enter message to send : ")
	A = 59
	i = 1 
	while True:
		if (G**i)%P == A:
			break
		i = i + 1
	print "K value is " + str(i)
	
	B = ((Y**i)*M) % P
	
	print "C2 value " + str(B)
P = input("Enter Prime Number 1 : ")
G = input("Enter Prime Number 2 : ")

X = input("Enter Random X value (Privatekey) : ")

# Y = (G**X) % P uncomment to find the public key

Y = 3

print "Public Keys"
print "P ==> " + str(P)
print "G ==> " + str(G)  
print "Y ==> " + str(Y)

#Sent to Alice(Public Keys)
sendToA(P,G,Y)
