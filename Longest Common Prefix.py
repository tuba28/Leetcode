# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs : 
            return ""
        
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith (prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

            
