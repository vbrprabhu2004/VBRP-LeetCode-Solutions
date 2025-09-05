from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        # Mark key as most recent: remove & reinsert
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        if key in self.cache:
            # Remove existing key first to update order
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used (first) key
            self.cache.popitem(last=False)
        # Insert key as most recent
        self.cache[key] = value