"""Data fetcher module for rxgemini"""

import functools


def data_fetcher(func):
    @functools.wraps
    def wrapper_fetcher(*args, **kwargs):
        
