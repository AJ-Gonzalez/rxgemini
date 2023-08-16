"""Sample project showcasing RX Gemini usage"""

from rxgemini.fetcher import data_fetcher

# RXGEMINI fetcher off


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


if __name__ == "__main__":
    print("RX Gemini showcase")
    add_numbers(1, 2)
