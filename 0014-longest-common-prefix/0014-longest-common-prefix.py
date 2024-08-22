class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # loop through an array
        # check ith letter of all x words
        # if they are equal, append that letter to a result string
        # if not, return whatever is in the string

        result = ""
        # grab the first index
        # grab its first letter
        # check if its equal to the first letter of the rest of the words in the loop
        # if it is, append it to result string

        # --- EDGECASES ---
        # if strings only contain ""
        if "" in strs:
            return result

        i = 0
        while i < len(strs[0]):
            # checking if each string has the same length at given index point
            for st in strs:
                # print('last index:', st.index(st[len(st)-1]))
                if i > st.rindex(st[-1]):
                    return result
            char = strs[0][i]
            for s in range(1, len(strs)):
                if char == strs[s][i]:
                    print(char, '==', strs[s][i])
                    continue
                else:
                    return result
            result += char
            i += 1
        return result

            