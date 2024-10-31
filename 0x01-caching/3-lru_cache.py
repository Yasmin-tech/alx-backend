#!/usr/bin/env python3
''' a class LRUCache implementation that inherits from
    BaseCaching and is a caching system.
    '''

from typing import Dict
BaseCaching = __import__('base_caching').BaseCaching


def shift_left(start_index: int, item_dict: Dict[int, str]) -> None:
    '''
        a helper function.
        Shift elements to the left to indicate that the element at
        key (0) is least used, and the element at index (MAX_ITEMS - 1)
        is most used
        '''
    last_index = len(item_dict) - 1
    count = start_index
    while count < last_index:
        item_dict[count] = item_dict[count + 1]
        count += 1
    return count


class LRUCache(BaseCaching):
    ''' A LRU <Least Recently Used> caching system.
        This caching system has a limit MAX_ITEMS = 4
        The least used item in self.cache_data will be removed.
        The item is recently used if it was added or updated
    '''
    def __init__(self) -> None:
        ''' Initialize an instance '''
        super().__init__()
        self.least_used_items = {}

    def put(self, key: str, value: any) -> None:
        ''' Add key-value pair to cache '''
        if key and value:
            if key in self.cache_data:
                # Update the value and move the key to the
                # most recently used position
                self.cache_data[key] = value
                start_index = 0
                for k, v in self.least_used_items.items():
                    if v == key:
                        start_index = k
                        break
                idx = shift_left(start_index, self.least_used_items)
                self.least_used_items[idx] = key
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Remove the least recently used item
                    least_used_item_key = self.least_used_items[0]
                    shift_left(0, self.least_used_items)
                    self.least_used_items[self.MAX_ITEMS - 1] = key
                    del self.cache_data[least_used_item_key]
                    print('DISCARD:', least_used_item_key)
                else:
                    curr_index = len(self.least_used_items)
                    self.least_used_items[curr_index] = key
                self.cache_data[key] = value

    def get(self, key: str) -> any:
        ''' Retrieve value from cache '''
        if key in self.cache_data:
            start_index = 0
            for k, v in self.least_used_items.items():
                if v == key:
                    start_index = k
                    break
            idx = shift_left(start_index, self.least_used_items)
            self.least_used_items[idx] = key
            return self.cache_data[key]
        return None
