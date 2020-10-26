#!/usr/bin/env python3
"""
LRU Caching
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Least recently used
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.cache_time = {}
        self.access_history = 0

    def put(self, key: str, item: str):
        """Add an item in the cache
        """
        if (key is not None and item is not None):
            self.cache_time[key] = self.access_history
            self.cache_data[key] = item
            self.access_history += 1
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                old_key = min(
                    self.cache_time.keys(),
                    key=lambda k: self.cache_time[k]
                )
                self.cache_data.pop(old_key)
                self.cache_time.pop(old_key)
                print("DISCARD: " + str(old_key))

    def get(self, key: str):
        """ Get an item by key
        """
        if (key is None or key not in self.cache_data):
            return None
        self.cache_time[key] = self.access_history
        self.access_history += 1
        return self.cache_data[key]
