class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        present_characters = []
        all_characters = []


        # Loop through characters in the first string only
        for i in range(len(strs[0])):
            char = strs[0][i]
            all_characters.append(char)


            # Check if the character at this index is the same in all other strings
            if all(i < len(word) and word[i] == char for word in strs[1:]):
                present_characters.append(char)
            else:
                break  # Stop at the first mismatch



        
        unique_common_chars = []
        for ch in present_characters:
                unique_common_chars.append(ch)

        return "".join(unique_common_chars)