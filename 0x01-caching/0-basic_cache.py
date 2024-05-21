#!/usr/bin/env python3
""" Basic caching module
"""
from base_caching import BaseCaching
from typing import Any, Optional


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - Caching: save data with key and value
    """
    def put(self, key: str, item: Any) -> None:
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key: str) -> Optional[Any]:
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
