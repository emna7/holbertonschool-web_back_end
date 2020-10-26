#!/usr/bin/env python3
"""
basic dictionary
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic cache
    """
    def put(self, key, item):
        """add an item
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """get an item
        """
        if (key in self.cache_data):
            return self.cache_data[key]
        return None
