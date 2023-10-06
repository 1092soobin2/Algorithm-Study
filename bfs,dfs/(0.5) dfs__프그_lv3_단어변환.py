from collections import defaultdict, deque


def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    len_word = len(begin)
    def count_diff(word1, word2):
        diff = 0
        for i in range(len_word):
            if word1[i] != word2[i]:
                diff += 1
        return diff

    adj_dict = defaultdict(list)
    len_word_list = len(words)
    for i in range(len_word_list):
        for j in range(i + 1, len_word_list):
            if count_diff(words[i], words[j]) == 1:
                adj_dict[words[i]].append(words[j])
                adj_dict[words[j]].append(words[i])
        if count_diff(words[i], begin) == 1:
            adj_dict[begin].append(words[i])
            

    def bfs():
        
        queue = deque([])
        visited_dict = dict()
        
        for word in adj_dict[begin]:
            queue.append(word)
            visited_dict[word] = 1
        
        while queue:

            curr_word = queue.popleft()
            curr_dist = visited_dict[curr_word]
            
            if curr_word == target:
                return curr_dist
            
            for word in adj_dict[curr_word]:
                if word not in visited_dict:
                    visited_dict[word] = curr_dist + 1
                    queue.append(word)
                
        return 0

    return bfs()
        
        
        
        
