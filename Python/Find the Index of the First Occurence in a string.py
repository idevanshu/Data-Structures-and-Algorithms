def strStr(haystack,needle):
        leng = len(needle)
        for i in range(len(haystack) - leng + 1):
            if haystack[i:i+leng] == needle:
                return i
        return -1

        ### Using the power of python.
        """
        index = haystack.find(needle)
        return index
        """
        

print(strStr(haystack = "sadbutsad", needle = "sad"))
print(strStr(haystack = "leetcode", needle = "leeto"))
