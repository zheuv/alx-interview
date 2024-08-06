    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters in the file.

    Operations:
    - Copy All (can be used multiple times, but must paste at least once before copying again)
    - Paste

    Parameters:
    n (int): The number of 'H' characters needed in the file.

    Returns:
    int: The minimum number of operations required to achieve n 'H' characters.
         If n is impossible to achieve, return 0.
    """
