#User inputs string
string = input()

#Function finding the first recurring character
def frc(s):

    a = []

    for i, c in enumerate(s):
        #If the character c is in the list a
        if c in a:
            print("The repeating character is: {}".format(c))
            #Finding the initial position of the character in the string
            for z, d in enumerate(a):
                if(d == c):
                    print(z)
                    return z

        else:
            #If there are no characters equal to c, add it to the array
            a.append(c)

    return "No repeaitng characters"

frc(string)
