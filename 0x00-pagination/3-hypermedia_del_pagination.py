#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''
            The goal of this function is that if between two queries,
            certain rows are removed from the dataset,
            the user does not miss items from dataset when changing page
            '''
        assert isinstance(index, int)
        assert isinstance(page_size, int)
        assert index >= 0
        assert index < len(self.__dataset)

        respons = {}
        data = []
        end_index = index
        count = 1

        # print(self.__indexed_dataset)
        while count <= page_size:
            result = self.__indexed_dataset.get(end_index)
            if result:
                # print('result', result)
                data.append(result)
                count = count + 1
                # print('count', count)
            end_index = end_index + 1
            # print('end_index', end_index)
            if end_index == len(self.__dataset):
                break
        respons['index'] = index
        respons['data'] = data
        respons['page_size'] = len(data)
        respons['next_index'] = end_index

        return respons
