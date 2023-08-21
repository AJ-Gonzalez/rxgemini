"""Sample project showcasing RX Gemini usage"""

from rxgemini.fetcher import data_fetcher

# RXGEMINI fetcher on


@data_fetcher
def add_numbers(num1: int, num2: int):
    """

    Example function to showcase fetcher decorator usage

    Args:
        num1 (int): Number
        num2 (int): Other number
    """
    example_sum = num1 + num2
    print("Sum: ", example_sum)


@data_fetcher
def a_function(string: str) -> int:
    """
    Example fucntion with a return value

    Args:
        string (str): String of text

    Returns:
        int: Length
    """
    return len(string)


@data_fetcher
def b_function(string: str, sample_kwarg: bool = True) -> int:
    """
    Example fucntion with a return value

    Args:
        string (str): String of text

    Returns:
        int: Length
    """
    if sample_kwarg:
        return len(string)

    return None


if __name__ == "__main__":
    print("RX Gemini showcase")
    add_numbers(1, 2)
    a_function("Example string")
    b_function("sample string again", sample_kwarg=False)
