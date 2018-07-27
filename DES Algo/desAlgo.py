
# Get the 10 input key from the user

inputKey = raw_input("Enter the key of length 10 : ")

randomTenPermuteUtilList = [ 3, 5 , 2 , 7 , 4 , 10 , 1 , 9 , 8 , 6 ]

counter = 0

permutedKey = ""

while counter < len(inputKey):
	permutedKey = permutedKey + inputKey [ randomTenPermuteUtilList [ counter ] - 1 ]
	counter = counter + 1

print "\nInitial Permutation Key is " + permutedKey + "\n"

counter = 0

permuteKeyLeft = ""
permuteKeyRight = ""

while counter < 5:
	if counter == 4:
		permuteKeyLeft = permuteKeyLeft + permutedKey [ 0 ]
	else:
		permuteKeyLeft = permuteKeyLeft + permutedKey [ counter + 1 ]
	counter = counter + 1

while counter < 10:
        if counter == 9:
                permuteKeyRight = permuteKeyRight + permutedKey [ 5 ]
        else:
                permuteKeyRight = permuteKeyRight + permutedKey [ counter + 1 ]
        counter = counter + 1

newPermutedKey = permuteKeyLeft + permuteKeyRight

print "\nNew Key after LS-1 is " + newPermutedKey + '\n'

randomEightPermuteUtilList = [ 6 , 3 , 7 , 4 , 8 , 5 , 10 , 9 ]

finalPermutedKey1 = ""

counter = 2

while counter < len(newPermutedKey):
	finalPermutedKey1 = finalPermutedKey1 + newPermutedKey[ randomEightPermuteUtilList [ counter - 2 ] - 1 ]
	counter = counter + 1

print "\n Final Key K1 is " + finalPermutedKey1 + '\n'


counter = 0

permuteKeyLeft = ""
permuteKeyRight = ""

while counter < 5:
        if counter == 4:
                permuteKeyLeft = permuteKeyLeft + permutedKey [ 1 ]
        elif counter == 3:
		permuteKeyLeft = permuteKeyLeft + permutedKey [ 0 ]
	else:
                permuteKeyLeft = permuteKeyLeft + permutedKey [ counter + 2 ]
        counter = counter + 1

counter = 5

while counter < 10:
        if counter == 9:
                permuteKeyRight = permuteKeyRight + permutedKey [ 6 ]
        elif counter == 8:
		permuteKeyRight = permuteKeyRight + permutedKey [ 5 ]
	else:
                permuteKeyRight = permuteKeyRight + permutedKey [ counter + 2 ]
        counter = counter + 1

newPermutedKey = permuteKeyLeft + permuteKeyRight

print "New Key after LS-2 : " + newPermutedKey + '\n'

finalPermutedKey2 = ""

counter = 2

while counter < len(newPermutedKey):
        finalPermutedKey2 = finalPermutedKey2 + newPermutedKey[ randomEightPermuteUtilList [ counter - 2 ] - 1 ]
        counter = counter + 1

print "\n Final Key K2 is " + finalPermutedKey2 + '\n'

inputText = raw_input("Enter input text of length 8 : ")

counter = 0
permutedInputText = ""

while counter < len(inputText):
	permutedInputText = permutedInputText + inputText[ randomEightPermuteUtilList [ counter ] - 3 ]
	counter = counter + 1

print "\n P-8 for input text : " + permutedInputText + '\n'

permutedInputTextRight = ""
permutedInputTextLeft = ""

counter = 0

while counter < len(permutedInputText):
	if counter < 4:
		permutedInputTextLeft = permutedInputTextLeft + permutedInputText[counter]
	else:
		permutedInputTextRight = permutedInputTextRight + permutedInputText[counter]
	counter = counter + 1

print "\n Left Half of P-8 Input Text : " + permutedInputTextLeft + '\n'
print "\n Right Half of P-8 Input Text : " + permutedInputTextRight + '\n'

