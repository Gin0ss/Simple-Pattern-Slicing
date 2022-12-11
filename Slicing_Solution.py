#FooBar challenge #1: Find the largest amount of equal slices
#from a given array(Pattern) of characters ranging from a-z with a common pattern
#Example Input: abcabcabcabc (4 sets of abc)
#Example Output: Pattern abcabcabcabc can be divided 4 times equally as abc
def solution(s): #s = input pattern
   i = 0
   maxCount = 1 #Initialise max amount of characters in current pattern
   maxPattern = s[:-1] #Takes 1 letter of the end of string
   
   for char in s: # Loop for every character in pattern
      i-=1 #i = Pattern slicing index
      count = 0 #Number of characters in current pattern
      pattern = s[:i] #Current pattern = sliced input pattern from the number of i spaces from the start

      if(len(pattern) > 0): #If the length of the pattern is more than 0
         if(len(s) % len(pattern) == 0): #If the length of input pattern is not divisible by current pattern
            count = int(len(s) / len(pattern)) #Number of character in current pattern = length of input pattern
                                               #divided by length of current pattern
            if(count > maxCount and pattern * s.count(pattern) == s): #If current amount of characters in pattern is greater
                                                                      #than last patterns length and current pattern put next to eachother
                                                                     #the amount of time the pattern has been detected
                                                                     #is the same as the pattern inputted then the current pattern is valid
               maxCount = count #New maximum number of instances of current
                                 #pattern is equal to current pattern frequency
               maxPattern = pattern #Current pattern with the largest frequency is the new maximum
                                 #number of subpatterns in input
   return maxCount #When the loop is over and iterated through each possible pattern return
                  #the final maximum frequency of the largest pattern that could be divided by the input


inp = input("Input: ") #Input pattern to be divided
print("Pattern: '{0}' can be divided {1} time(s) ".format(inp, solution(inp))) #Display result of code
                                          #showing input pattern and number of times it can be divided
                                          #equally by the largest pattern possible
