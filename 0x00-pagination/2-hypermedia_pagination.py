#!/usr/bin/env python3
'''
    This script contains the class Server
    server object has the attribute 'get_page'
    that returns a paginated response from the file
    <Popular_Baby_Names.csv>.
    '''


import csv
from typing import Tuple, List, Dict, Union
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

    def get_hyper(self,
                  page: int = 1,
                  page_size: int = 10
                  ) -> Dict[str, Union[int, List[int], None]]:
        ''' Returns a dictionary containing the following key-value pairs:

            - page_size: the length of the returned dataset page
            - page: the current page number
            - data: the dataset page (equivalent to return from previous task)
            - next_page: number of the next page, None if no next page
            - prev_page: number of the previous page, None if no previous page
            - total_pages: the total number of pages in the dataset
                as an integer
            '''
        response = {}
        data = self.get_page(page=page, page_size=page_size)

        next_page = None
        total_pages = len(self.__dataset)
        if page < total_pages / page_size:
            next_page = page + 1

        prev_page = None

        if page > 1:
            prev_page = page - 1

        response['page_size'] = len(data)
        response['page'] = page
        response['data'] = data
        response['next_page'] = next_page
        response['prev_page'] = prev_page
        response['total_pages'] = total_pages

        return response
