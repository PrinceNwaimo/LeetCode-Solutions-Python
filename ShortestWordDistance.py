import sys 

class ShortestWordDistance(object):
    def shortestDistance(self, words, word1, word2):         
        """:type words: List[str]
           :type word1: str         
           :type word2: str
           :rtype: int """
        word2_positions = []
        word1_positions = []
        min_distance = sys.maxsize
        
        for i in range(len(words)):
            if word1 == words[i]:
                word1_positions.append(i)
            if word2 == words[i]:
                word2_positions.append(i)
            
            for pos1 in word1_positions:
                for pos2 in word2_positions:
                    min_distance = min(min_distance, abs(pos1 - pos2))
        
        return min_distance
                    