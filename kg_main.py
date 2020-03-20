import sys

def check_lens(s1_len, s2_len):
    """Check the length of the strings to ensure property (1) of a one-to-one mapping. Returns boolean."""
    if s1_len <= s2_len and s1_len > 0:
        return True
    return False

def generate_freqs(s1):
    """Generate the frequencies of each character in s1 to help determine 
    if a one-to-one mapping is possible. Returns dictionary."""
    freqs = {}
    for c in s1:
        if c not in freqs:
            freqs[c] = 1
        else:
            freqs[c] += 1
    return freqs

def frequency_check(freqDict):
    """Check to ensure there are unique characters in s1 using the frequency dictionary
    because two of the same characters cannot possibly map one-to-one. Returns boolean."""

    for value in freqDict.values():
        if value > 1:
            return False
    return True


# We are only considering two strings for the one-to-one mapping
# Exit if there aren't only two strings on the command line

if len(sys.argv) != 3:
    sys.exit("Please include two command-line arguments to check if there is a one-to-one mapping")

# Properties of a one-to-one mapping:
#   (1) The length of s1 must be less than or equal to the length of s2.
#       (1a) Only checking for one-to-one, not onto.
#   (2) There can be no repeat characters in s1.
#       (2a) Duplicate characters in s1 aren't treated the same as duplicate characters in s2
#           thus we don't care about duplicates in s2 i.e bar maps one-to-one to foo but foo 
#           doesn't map one-to-one with bar
  
# Getting the command line args
argsList = list(sys.argv)

s1, s2 = argsList[1], argsList[2]

print(s1)
print(s2)

#Resolving Property (1)
len_check = check_lens(len(s1), len(s2))

if not len_check:
    #If we are here, s1's length is greater than s2's length so a one-to-one mapping isn't possible
    sys.exit("False")


#Resolving Property (2)
freq = generate_freqs(s1)

for x,y in freq.items():
    print(x,y)

freq_check = frequency_check(freq)

if not freq_check:
    sys.exit("False")

#If we get this far, s1 can be mapped one-to-one to s2 
sys.exit("True")