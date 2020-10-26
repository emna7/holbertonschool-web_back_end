#!/usr/bin/env python3
"""
LIFO Caching
"""


from base_caching import BaseCaching
from datetime import datetime


class LIFOCache(BaseCaching):
    """Last In Fist Out
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.cache_time = {}

    def put(self, key: str, item: str):
        """Add an item in the cache
        """
        if (key is not None and item is not None):
            self.cache_time[key] = datetime.now()
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                my_list = [
                    k for k, v in sorted(
                        self.cache_time.items(),
                        key=lambda p: p[1],
                        reverse=True
                        )]
                del self.cache_data[my_list[1]]
                del self.cache_time[my_list[1]]
                print("DISCARD: " + str(my_list[1]))

    def get(self, key: str):
        """ Get an item by key
        """
        if (key is None or key not in self.cache_data):
            return None
        return self.cache_data[key]
