class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Algo uses sorting each word and keeping track in a hash table (dict)
        """
        words_dict = dict()

        for i, word in enumerate(strs):
            # takes a word, sorts it and keep it in temp variable
            copied_word = "".join(sorted(word))

            # checks the temp word with the dictionary "words_dict"
            if copied_word in words_dict:
                words_dict[copied_word].append(word)
            else:
                words_dict[copied_word] = [word]

        anagrams = []
        # scans through dict and stores in a resultant list
        for i in words_dict:
            anagrams.append(words_dict[i])

        return anagrams
