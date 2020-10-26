#!/usr/bin/env python3
"""
MRU Caching
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Most recently used
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
                my_list = [
                    k for k, v in sorted(
                        self.cache_time.items(),
                        key=lambda p: p[1],
                        reverse=True
                        )]
                self.cache_data.pop(my_list[1])
                self.cache_time.pop(my_list[1])
                print("DISCARD: " + str(my_list[1]))

    def get(self, key: str):
        """ Get an item by key
        """
        if (key is None or key not in self.cache_data):
            return None
        self.cache_time[key] = self.access_history
        self.access_history += 1
        return self.cache_data[key]
