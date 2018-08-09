
def sendToA ( P , G , Y ):
	print "In Alice"
	M = input("Enter message to send : ")
	K = input("Enter random K value : ")
	
	A = (G**K) % P
	B = ((Y**K)*M) % P
	
	print "Cipher for Message is "
	
	print "A ==> " + str(A)
	print "B ==> " + str(B)
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
