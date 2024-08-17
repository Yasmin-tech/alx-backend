#!/usr/bin/env python3
''' This script contains a simple helper function that return a tuble of
    of the indexes of the start and end of return in a list for a
    particular pagination parameters.
    '''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    ''' A function should return a tuple of size two containing
        a start index and an end index corresponding to the range of
        indexes to return in a list for those particular pagination parameters
        '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
