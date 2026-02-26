class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = []

        list1 = list(word1)
        list2 = list(word2)

        for i in range(0, min(len(list1), len(list2))):œ
            result.append(list1[i])
            result.append(list2[i])
            
        left = list1 if len(list1) > len(list2) else list2
        result.extend(left[i+1:])
        
        final = ''.join(result)
        
        return final

