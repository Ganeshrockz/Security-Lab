
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def passPublicKeyToB( n ):
	
	print "In B \n"
	inputMessage = raw_input("Enter message : ")

	counter = 0
	encryptedCipherList = []
	
	while counter < len(inputMessage):
		value = ( ord(inputMessage[counter])**n ) % n
		encryptedCipherList.append( value )
		counter = counter + 1 
	return encryptedCipherList


primeNumber1 = input("Enter a prime number : ")

primeNumber2 = input("Enter another prime number : ")

n = primeNumber1 * primeNumber2

mod1 = primeNumber1 - 1
mod2 = primeNumber2 - 1

mulInverseOfPrimeNumber1 = multiplicative_inverse( primeNumber1 , mod2 )
mulInverseOfPrimeNumber2 = multiplicative_inverse( primeNumber2 , mod1 )

print "P' = " + str(mulInverseOfPrimeNumber1)

print "Q' = " + str(mulInverseOfPrimeNumber2)

encryptedCipherFromB = passPublicKeyToB( n )

counter = 0

decryptedString = ""

while counter < len(encryptedCipherFromB):
	value = chr((encryptedCipherFromB[counter] ** mulInverseOfPrimeNumber2 ) % primeNumber1)
	counter = counter + 1
	decryptedString = decryptedString + value

print decryptedString   
