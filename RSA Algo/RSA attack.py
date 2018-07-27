import random


def computeGCD( eValue, phiValue):

    while phiValue != 0:
        eValue , phiValue = phiValue , eValue % phiValue
    
    return eValue


def attackTheMessage( cipherList , e , n ):

	m = 26
	counter = 0
	decryptionList = []
	while counter < m:
		value = (counter**e)%n
		decryptionList.append(value)
		counter = counter + 1
	counter = 0
	hackedText = ""
	while counter < len(cipherList):
		innercounter = 0
		while innercounter < len(decryptionList):
			if cipherList[counter] == decryptionList[innercounter]:
				hackedText = hackedText + chr(innercounter + 97)
				break
			innercounter = innercounter + 1
		counter = counter + 1

	print "ATTACKED!!!!!\n"
	print hackedText

inputPrimeNumberOne = input("Enter a Prime Number : ")

inputPrimeNumberTwo = input("Enter another Prime Number : ")

nValue = inputPrimeNumberOne * inputPrimeNumberTwo

phiValue = (inputPrimeNumberOne-1)*(inputPrimeNumberTwo-1)

eValue = random.randrange(1,phiValue)

gcdValue = computeGCD( eValue,phiValue )

while gcdValue != 1:
    eValue = random.randrange(1,phiValue)
    gcdValue = computeGCD( eValue,phiValue )

print "The Public key is e = " + str(eValue) + " n = " + str(nValue)

inputMessage = raw_input("Enter message to be passed : ")

counter = 0

encryptedCipherList = []

while counter < len(inputMessage):
    value = ((ord(inputMessage[counter])-97) ** eValue) % nValue
    encryptedCipherList.append(value)
    counter = counter + 1


attackTheMessage( encryptedCipherList , eValue , nValue )

