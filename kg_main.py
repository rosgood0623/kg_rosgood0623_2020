import sys

def check_lens(s1_len, s2_len):

    if s1_len <= s2_len:
        return True

    return False
    
# We are only considering two strings for the one-to-one mapping
# Exit if there aren't only two strings on the command line

if len(sys.argv) != 3:
    sys.exit("Please include two command-line arguments to check if there is a one-to-one mapping")

# Properties of a one-to-one mapping:
#   (1) The length of s1 must be less than or equal to the length of s2.
#       (1a) Only checking for one-to-one, not onto.
#   (2) There can be no repeat characters in s1.
#   (3)  

# Getting the command line args
argsList = list(sys.argv)

s1, s2 = argsList[1], argsList[2]

print(s1)
print(s2)

#Resolving Property (1)
len_check = check_lens(len(s1), len(s2))

if not len_check:
    #If we are here, s1's length is greater than s2's length so a one-to-one mapping isn't possible
    sys.exit("false")


