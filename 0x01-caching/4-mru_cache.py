#!/usr/bin/env python3
""" MRU Model """
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ Inherets from BaseCaching
     MRU algorithm """

    def __init__(self):
        """ Inintialize Cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds the item to the cache with the given key.
         LIFO Algorithm"""
        if key is None and item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = next(reversed(self.cache_data))
                print(f"DISCARD: {mru_key}")
                self.cache_data.pop(mru_key)
        self.cache_data[key] = item

    def get(self, key):
        """ Must return the value associated
        with the key from the cache dictionary """
        if key is None:
            return None
        return self.cache_data.get(key)
