def mostWordsFound(sentences):
    count = 0
    for i in range(len(sentences)):
        sentence = sentences[i].split(" ")
        count = max(count, len(sentence))   
    return count


print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))