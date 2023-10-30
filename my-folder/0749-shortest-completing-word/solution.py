class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_chars = [c.lower() for c in licensePlate if c.isalpha()]
        license_counts = collections.Counter(license_chars)

        shortest_word = None
        shortest_length = float('inf')

        # Iterate through words and find the shortest completing word
        for word in words:
            word_chars = [c.lower() for c in word if c.isalpha()]
            word_counts = collections.Counter(word_chars)

            # Check if word is a completing word
            valid_word = True
            for char, count in license_counts.items():
                if word_counts[char] < count:
                    valid_word = False
                    break
            
            # If valid and shorter, update shortest_word and shortest_length
            if valid_word and len(word) < shortest_length:
                shortest_word = word
                shortest_length = len(word)

        return shortest_word











