#!/usr/bin/env python3
''' a class BasicCache that inherits from BaseCaching and is a caching system.
    '''


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' A simple caching system.

        This caching system doesn’t have limit

        Instance Method:
        put: to add key value pair
        get: to retrive the value from the system
        '''
    def __init__(self) -> None:
        ''' inisialize an 'nstance
            '''
        super().__init__()

    def put(self, key: str, value: any) -> None:
        ''' store the key value pair in the caching system (dictionary)
            '''
        if key and value:
            self.cache_data[key] = value

    def get(self, key: str) -> any:
        ''' Retrieve the associated value if the key is not none
            and exists in the self.cache_data. Otherwise, return None
            '''
        if key:
            return self.cache_data.get(key)
        return None
