class MyHashMap:

    def __init__(self):
        self.size = 1000
        # Initialize an empty hashmap array
        self.hashmap = [[] for _ in range(self.size)]

    def _get_hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self._get_hash(key)
        bucket = self.hashmap[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                 # If key already exists, update the value
                bucket[i] = (key, value)
                return
        # If key doesn't exist, add a new (key, value) pair
        bucket.append((key, value))

    def get(self, key: int) -> int:
        hash_key = self._get_hash(key)
        bucket = self.hashmap[hash_key]
        for k, v in bucket:
            # If key found, return the corresponding value
            if k == key:
                return v
        # If key not found, return -1
        return -1

    def remove(self, key: int) -> None:
        hash_key = self._get_hash(key)
        bucket = self.hashmap[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
