#!/usr/bin/env python3
""" LRU Model """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Inherets from BaseCaching
     Last In First Out System """

    def __init__(self):
        """ Inintialize Cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds the item to the cache with the given key.
         LRU Algorithm"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = next(iter(self.cache_data))
                print(f"DISCARD: {lru_key}")
                self.cache_data.pop(lru_key)
        self.cache_data[key] = item

    def get(self, key):
        """ Must return the value associated
        with the key from the cache dictionary """
        if key is None or key not in self.cache_data:
            return None

        """ Move the accessed item to the end
        to mark it as recently used  """
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
