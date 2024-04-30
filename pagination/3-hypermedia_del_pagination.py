#!/usr/bin/env python3
""" Simple pagination function """


import csv
from typing import Dict, List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """ Server class to paginate a database of popular baby names """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialize the server instance """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
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
        """ Get the requested page with hypermedia """
        assert index is not None and index >= 0
        assert page_size > 0

        dataset = self.indexed_dataset()
        data = []
        next_index = index + page_size
        for i in range(index, next_index):
            if dataset.get(i) is not None:
                data.append(dataset[i])

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index if next_index < len(dataset) else None
        }
