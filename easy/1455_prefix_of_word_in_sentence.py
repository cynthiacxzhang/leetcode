# Prefix of Word in Sentence

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """

        # Brainstorm
        """
        Python method - sentencestring.split
        - this splits the sentence string into a list of words 
        - separates based on spaces
        
        Compare the prefix with every word in the list
        - for loop through however many words there are in the list
        - return index of the word in the split words list

        """

        words_list = sentence.split()

        for i in range(len(words_list)):
            current_word = words_list[i]
            print(current_word)

            # setting a checkpoint
            valid = True

            # need the min because 
            for j in range(len(searchWord)):

                # catching 
                if j >= len(current_word):
                    valid = False
                    break

                if current_word[j] != searchWord[j]: 
                    valid = False # setting checkpoint to False
                    break
                j += 1
            
            # if valid is false, that means the loop was broken out of
            # e.g. the previous word was not a valid prefix
            if valid == True:
                return i+1
            i += 1
        return -1

        
# Better time complexity - using build in method string.startswith
class Solution2(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """

        # Brainstorm
        """
        Python method - sentencestring.split
        - this splits the sentence string into a list of words 
        - separates based on spaces
        
        Compare the prefix with every word in the list
        - for loop through however many words there are in the list
        - return index of the word in the split words list

        """

        words_list = sentence.split()

        for i in range(len(words_list)):
            current_word = words_list[i]
            print(current_word)

            # need the min because 
            for j in range(len(searchWord)):
                if current_word.startswith(searchWord):
                    return i+1  # 1-indexed, not 0 indexed
            
            i += 1
        return -1
      