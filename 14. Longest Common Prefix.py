class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        x = ""
        z = strs[0]
        for letter in range(len(z)):
            for word in strs:
                if letter < len(word):
                    if z[letter] == word[letter]:
                        continue
                    else: 
                        return x
                else:
                    return x
            x += z[letter]
        return x
            


    


        
