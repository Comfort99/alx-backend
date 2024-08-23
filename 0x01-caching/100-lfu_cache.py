#!/usr/bin/env python3
""" LFU MODEL """
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching
    and implements a caching system with
    LFU (Least Frequently Used) eviction policy."""

    def __init__(self):
        """ Initialize cache_data (class)"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.freqs = defaultdict(int)  # Tracks the frequency of each key

    def put(self, key, item):
        """
        Adds the item value to the key in self.cache_data.
        If the cache exceeds MAX_ITEMS, it discards the least
        frequently used item.If there's a tie in frequency, it
        discards the least recently used item among them.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict the least frequently used item
                self._evict_least_frequently_used()
            self.cache_data[key] = item
            self.freqs[key] = 1
        # Move the updated or newly added key (value) to the end
        self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Returns the value associated with key in self.cache_data.
        Updates the frequency of the key.
        """
        if key is None or key not in self.cache_data:
            return None
        self._update_frequency(key)
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """
        updates the frequency count for the given key
        """
        self.freqs[key] += 1

    def _evict_least_frequently_used(self):
        """
        Evicts the least frrequently used item from cache
        If multiple items have the same frequency,
        evicts the least recently used among them
        """
        # find the minimum frequency
        min_freq = min(self.freqs.values())
        # find the keys with the minimum frequency
        items = self.freqs.items()
        keys_min_freq = [k for k, freq in items if freq == min_freq]

        for key in self.cache_data:
            if key in keys_min_freq:
                self.cache_data.pop(key)
                self.freqs.pop(key)
                print(f"DISCARD: {key}")
                break
