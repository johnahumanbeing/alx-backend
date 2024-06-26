#!/usr/bin/env python3
""" MRU Caching module
"""
from base_caching import BaseCaching
from typing import Any, Optional


class MRUCache(BaseCaching):
    """ MRU Caching class
    """
    def put(self, key: Any, item: Any) -> None:
        """ Add an item in the cache
            - Args:
                - key: key to look for
                - item: value to add for the key
        """
        if not key or not item:
            return
        new_cache_data = {key: item}
        if len(self.cache_data) == self.MAX_ITEMS:
            key_to_remove = list(self.cache_data.keys())[-1]
            self.cache_data.pop(key_to_remove)
            print(f'DISCARD: {key_to_remove}')
        self.cache_data.update(new_cache_data)

    def get(self, key: Any) -> Optional[Any]:
        """ Gets cache data associated with given key
            and updates dict in accordance to MRU policy
            - Args:
                - key to look for
            - Return:
                - value associated with the key
        """
        cache_item = self.cache_data.get(key)
        if cache_item:
            self.cache_data.pop(key)
            self.cache_data.update({key: cache_item})
        return cache_item
