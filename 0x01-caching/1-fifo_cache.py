#!/usr/bin/env python3
""" FIFO MODEL """
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ Inherits from BaseCaching
    First in First Out System"""

    def __init__(self):
        """ Initialize the Cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds the item to the cache with the given key.
        FIFO Algorithm"""
        if key is None and item is None:
            return

        self.cache_data[key] = item

        """ first check if the dictionary is not full """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))
            print(f"Discard: {oldest_key}")
            self.cache_data.pop(oldest_key)

    def get(self, key):
        """ Must return the value associated
        with the key from the cache dictionary """
        if key is None:
            return None
        return self.cache_data.get(key)
