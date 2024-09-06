#!/usr/bin/env python3
''' a class FIFOCache implementation that inherits from
    BaseCaching and is a caching system.
    '''


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' A FIFO caching system.

        This caching system has a limit MAX_ITEMS = 4

        Instance Method:
        put: to add key value pair,
            If the number of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS,
            discard the first item put in cache (FIFO algorithm)
            and print DISCARD: with the key discarded.
        get: to retrive the value from the system
        '''
    def __init__(self) -> None:
        ''' inisialize an instance
            '''
        super().__init__()

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
                # get the first item if the system is full and remove it
                # sorted() function returns a list
                first_key = sorted(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print('DISCARD:', first_key)
            self.cache_data[key] = value

    def get(self, key: str) -> any:
        ''' Retrieve the associated value if the key is not none
            and exists in the self.cache_data. Otherwise, return None
            '''
        if key:
            return self.cache_data.get(key)
        return None
