
class Solution:
    # Function to convert the given string to Camel Case
    def convertToCamelCase(self, s):
        camel=""
        words=s.split()
        camel+=words[0]
        for i in range(1,len(words)):
            camel+=words[i].capitalize()
        return camel
        