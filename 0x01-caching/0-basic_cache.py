#!/usr/bin/env python3
""" Child Model """
from base_cache import BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching and
        is a basic caching system with no limit. """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adds the item to the cache with the given key."""
        if key and item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Must return the value associated
        with the key from the cache dictionary """
        if key is None:
            return None
        return self.cache_data.get(key)
