"""Sample project showcasing RX Gemini usage"""

from rxgemini.fetcher import data_fetcher

# RXGEMINI fetcher off


@data_fetcher
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)


if __name__ == "__main__":
    print("RX Gemini showcase")
    add_numbers(1, 2)
