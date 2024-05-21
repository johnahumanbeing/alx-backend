#!/usr/bin/env python3
""" FIFO caching module
"""
from base_caching import BaseCaching
from typing import Any, Optional


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - Caching: save data with FIFO algorithm
    """

    def __init__(self) -> None:
        """ Initialize
        """
        super().__init__()
        self.keys = []

    def put(self, key: str, item: Any) -> None:
        """ Adds data to cache based on FIFO policy
            - Args:
                - key: new entry's key
                - item: entry's value
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD:", discard)
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key: str) -> Optional[Any]:
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
