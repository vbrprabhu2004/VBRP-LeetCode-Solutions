from collections import defaultdict, OrderedDict

class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}               # key → (value, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq → OrderedDict(keys)

    def _update_freq(self, key):
        val, freq = self.key_to_val_freq[key]
        # Remove key from current freq list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1
        # Add key to next freq list
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key] = (val, freq + 1)

    def get(self, key):
        if key not in self.key_to_val_freq:
            return -1
        self._update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.key_to_val_freq:
            # Update value, then increase frequency
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update_freq(key)
            return
        if len(self.key_to_val_freq) >= self.capacity:
            # Remove LRU key with min frequency
            old_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[old_key]
        # Insert new key with freq = 1
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1