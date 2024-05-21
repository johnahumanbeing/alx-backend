#!/usr/bin/env python3
""" LIFO Caching module
"""
from base_caching import BaseCaching
from typing import Any, Optional


class LIFOCache(BaseCaching):
    """ LIFO Caching class
    """

    def __init__(self):
        """ Constructor method
        """
        super().__init__()
        self.cache_list = []

    def put(self, key: str, item: Any):
        """ Adds data to cache based on LIFO policy
            - Args:
                - key: new entry's key
                - item: entry's value
        """
        if key and item:
            if key in self.cache_data:
                self.cache_list.remove(key)
            self.cache_data[key] = item
            self.cache_list.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last = self.cache_list.pop(-2)
                del self.cache_data[last]
                print(f"DISCARD: {last}")

    def get(self, key: str) -> Optional[Any]:
        """ Gets cache data associated with given key
            - Args:
                - key to look for
            - Return:
                - value associated with the key
        """
        return self.cache_data.get(key, None)
