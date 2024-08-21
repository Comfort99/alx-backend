#!/usr/bin/env python3
""" MRU Model """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ Inherets from BaseCaching
     MRU algorithm """

    def __init__(self):
        """ Inintialize Cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds the item to the cache with the given key.
         LIFO Algorithm"""
        if key is None or item is None:
            return

        # If the key already exist update the position
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        else:
            # if the dictionary cache is full, remove the recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = next(reversed(self.cache_data))
                print(f"DISCARD: {mru_key}")
                self.cache_data.popitem(last=True)

        self.cache_data[key] = item

    def get(self, key):
        """ Must return the value associated
        with the key from the cache dictionary """
        if key is None:
            return None
        return self.cache_data.get(key)
