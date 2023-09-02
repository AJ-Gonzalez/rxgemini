"""Classification and Validation module"""

import math
import pickle

from rxgemini.log_handler import log_info


def index_finder(args_content: dict) -> int:
    """
    Complexity index finder.

    The complexity index is a aggregate measurement
    of the relative complexity of the inputs of a
    specific func/method call.

    We measure the complexity of each parameter's
    value by convering it to bytes and then
    eliminating duplicate bytes with set().
    By having only the unique bytes we get an
    approximate measure of the variations in how the
    value was stored, the more variations, the more
    complex it is.

    To avoid having to handle exceptions all byte
    conversions are done with pickle, and made
    iterable with bytearray, so they can be reduced
    with set.

    Then we list the bytes and get a len attribute.
    After that, we get the median len() of the set
    of parameters.

    This median len will be our complexity index.


    Args:
        args_content (dict): func/method call contents

    Returns:
        int: complexity index
    """
    indices = []
    for key, value in args_content.items():
        log_info(f"Evaluating complexity for: {key}")
        pickled_bytes = bytearray(pickle.dumps(value))
        set_val = set(pickled_bytes)
        param_index = len(set_val)
        indices.append(param_index)
        log_info(f"{key} has index: {param_index}")

    indices.sort()
    middle_index = len(indices)/2
    exact_middle_index = math.floor(middle_index)
    complexity_index = indices[exact_middle_index]
    log_info(f"Complexity index is: {complexity_index}")
    return complexity_index
