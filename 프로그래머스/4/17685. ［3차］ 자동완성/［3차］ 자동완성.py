def solution(words):
    answer = 0
    words.sort()
    len_words = len(words)
    
    def count_chars_for_uniqueness(i, word):
        count = 1
        for j in range(len(word)):
            unique = True
            if i > 0 and words[i-1][:j+1] == word[:j+1]:
                unique = False
            if i < len_words-1 and words[i+1][:j+1] == word[:j+1]:
                unique = False
            if unique:
                return j+1
        return len(word)
    
    for i in range(len_words):
        answer += count_chars_for_uniqueness(i, words[i])
    
    return answer