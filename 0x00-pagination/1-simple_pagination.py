#!/usr/bin/env python3
'''
    This script contains the class Server
    server object has the attribute 'get_page'
    that returns a paginated response from the file
    <Popular_Baby_Names.csv>
    '''


import csv
from typing import Tuple, List
import math


def index_range(page: int, page_size: int) -> Tuple[int]:
    ''' A function should return a tuple of size two containing
        a start index and an end index corresponding to the range of
        indexes to return in a list for those particular pagination parameters
        '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Return a paginated response of popular baby names
            - page with default value 1, page_size with default value 10
            -  both arguments are integers greater than 0
            - If the input arguments are out of range for the dataset,
                 an empty list should be returned
            '''
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        start, end = index_range(page, page_size)

        result = self.dataset()[start: end]
        return result
