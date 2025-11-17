class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        use a nested dictionary? 
        
        1 - loop to create frequency map of every string in strs
        2 - compare frequency maps, group ones that are equal?

        how are we grouping it? track index of the anagram? enumerate first?
        1 - enumerate to get (index, string at strs[w])
        2 - loop to create list of freq maps for every string in strs
        3 - iterate over this list, add to a map of results with 
            key = index, 
            val = [arr of strs with equivalent frequency maps]
        4 - return results list

        dictionary = {anagram: [indexes with that anagram value]}
        """
        
        # map that stores key = sorted string -> val = array of indexes
        groups = {}

        # store all indexes with the same anagram under the same hash location
        for string in strs:
            # sort string 
            # key = "".join(sorted(string)) # sorting the string is nlogn, what is more optimaL?
            

            # ascii frequency mapping
            freq_count = [0]*26
            for ch in string:
                idx = ord(ch) - ord('a')
                freq_count[idx] += 1

            key = tuple(freq_count)

            # if key dne yet, initialize it
            if key not in groups:
                groups[key] = []
            # append string instead of index, no need to append index
            groups[key].append(string)
            
        # final = []
        # for group in groups:
        #     final.append(groups[group]) 
        # return final
        
        return list(groups.values())





            
