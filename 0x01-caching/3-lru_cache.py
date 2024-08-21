#!/usr/bin/env python3
''' a class LRUCache implementation that inherits from
    BaseCaching and is a caching system
    '''


from typing import Dict
BaseCaching = __import__('base_caching').BaseCaching


def shif_left(start_index: int, item_dict: Dict[int, str]) -> None:
    '''
        a helper function.
        Sheft element to the list to indicated that element that has
        key (0) is least used , and element at index (MAX_ITEMS - 1)
        is most used
        '''
    # stop when you reach the last index, based 0
    last_index = len(item_dict) - 1
    count = start_index
    while count < last_index:
        item_dict[count] = item_dict[count + 1]
        count = count + 1


class LRUCache(BaseCaching):
    ''' A LRU <Least Recently Used> caching system.

        This caching system has a limit MAX_ITEMS = 4

        The Least used item in self.cache_data will be removed.
        The item is recently used if it was added or updated

        Instance Method:
        put: to add key value pair,
            If the number of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS,
            discard the least recently used item (LRU algorithm)
            and print DISCARD: with the key discarded.
        get: to retrive the value from the system
        '''
    def __init__(self) -> None:
        ''' inisialize an instance
            '''
        super().__init__()
        self.least_used_items = {}

    def put(self, key: str, value: any) -> None:
        ''' add key value pair,
            If the number of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS,
            discard the first item put in cache (FIFO algorithm)
            and print DISCARD: with the key discarded.
            '''

        if key and value:
            if len(self.cache_data) >= self.MAX_ITEMS \
                    and key not in self.cache_data:
                # get the least used if the system is full and remove it

                least_used_item_key = self.least_used_items[0]
                shif_left(0, self.least_used_items)
                self.least_used_items[self.MAX_ITEMS - 1] = key
                del self.cache_data[least_used_item_key]
                print('DISCARD:', least_used_item_key)
                self.cache_data[key] = value
            elif key in self.cache_data:
                start_index = 0
                for k, v in self.least_used_items.items():
                    if v == key:
                        start_index = k
                        break
                shif_left(start_index, self.least_used_items)
                self.least_used_items[self.MAX_ITEMS - 1] = key
                self.cache_data[key] = value
            else:
                self.cache_data[key] = value
                curr_index = len(self.least_used_items)
                self.least_used_items[curr_index] = key

        # print(self.least_used_items)

    def get(self, key: str) -> any:
        ''' Retrieve the associated value if the key is not none
            and exists in the self.cache_data. Otherwise, return None
            '''
        if key:
            if self.cache_data.get(key):
                start_index = 0
                for k, v in self.least_used_items.items():
                    if v == key:
                        start_index = k
                        break
                shif_left(start_index, self.least_used_items)
                self.least_used_items[self.MAX_ITEMS - 1] = key
                # print(self.least_used_items)
                return self.cache_data.get(key)
        return None
