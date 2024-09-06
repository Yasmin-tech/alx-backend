#!/usr/bin/env python3
"""Least Frequently Used caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with an LFU
    removal mechanism when the limit is reached
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency_cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the value and increment the frequency
            self.cache_data[key] = item
            self.frequency_cache_data[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequently used item
                key_to_remove = min(
                        self.frequency_cache_data,
                        key=self.frequency_cache_data.get)
                del self.cache_data[key_to_remove]
                del self.frequency_cache_data[key_to_remove]
                print('DISCARD:', key_to_remove)

            # Add the new item and set its frequency to 1
            self.cache_data[key] = item
            self.frequency_cache_data[key] = 1

        # print('cache_data:', self.cache_data)
        # print('frequency_cache_data:', self.frequency_cache_data)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is None or key not in self.cache_data:
            return None

        # Increment the frequency of the accessed item
        self.frequency_cache_data[key] += 1
        # print('cache_data:', self.cache_data)
        # print('frequency_cache_data:', self.frequency_cache_data)
        return self.cache_data[key]
