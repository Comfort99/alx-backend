#!/usr/bin/env python3
""" Module Pagination """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ A function that returns a Tuple
    that contains a start_index and end_index"""

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
