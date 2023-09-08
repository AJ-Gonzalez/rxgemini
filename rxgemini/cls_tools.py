"""Classification and Validation module"""

import math
import pickle
from operator import itemgetter

from rxgemini.log_handler import log_info
from rxgemini.constants import ICI_TEMPLATE


# i know this computationally sucks, but is the cost of not
# being able to manage numpy
# dependencies within python versions,
# and I still wanna support 3.7.4 bc enterprise.
def percentile(in_ls: list, percentile_var: float) -> list:
    """
    Returns a list with the desired percentile set

    Args:
        in_ls (list): Input list
        percentile_var (float): Percentile float

    Returns:
        list: percentile set
    """
    data_sorted = sorted(in_ls)  # Sort in ascending order
    print(percentile_var)
    index = math.ceil(percentile_var * len(data_sorted))
    print(len(data_sorted), index)

    return data_sorted[index]


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


def instance_ranking(instances: list):
    print(ICI_TEMPLATE)
    # TODO: Implement ranking from file name
    rank_ls: list = [(int(file_str.split("_")[0]), file_str)
                     for file_str in instances]
    sorted_rankings = (sorted(rank_ls, key=itemgetter(0)))
    rank_dict: dict = {int(elm[0]): elm[1] for elm in sorted_rankings}
    print(rank_dict)
    deciles = [percentile(rank_dict, clx/10) for clx in range(0, 10)]
    for idx, decile in enumerate(deciles):
        print(idx, decile)
    stats_dict = {"50th": percentile(rank_dict, 0.5),
                  "high": max(rank_dict),
                  "low": min(rank_dict),
                  "90th": percentile(rank_dict, 0.9),
                  "10th": percentile(rank_dict, 0.1),
                  "70th": percentile(rank_dict, 0.7),
                  "30th": percentile(rank_dict, 0.3),
                  "whole": list(rank_dict),
                  "raw": rank_dict}
    print(stats_dict)
