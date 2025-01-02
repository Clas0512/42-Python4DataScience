def ft_filter(func: callable, array: iter):
    """
    Custom filter function that applies a given function to each element in
    the iterable
    and yields only the elements that satisfy the function's condition.

    Args:
        func (callable): A function that returns a boolean value (True or
        False) to filter elements.
        array (iter): An iterable (e.g., list, tuple, etc.) that contains the
        elements to be filtered.

    Yields:
        Elements from the iterable for which the function returns True.
        If no function is provided, it filters out elements considered as
        False (e.g., empty strings, 0, etc.).

    Example:
        >>> list(ft_filter(lambda x: x > 2, [1, 2, 3, 4]))
        [3, 4]

        >>> list(ft_filter(None, [0, 1, 2, '', 'hello']))
        [1, 2, 'hello']
    """
    if func:
        yield from [x for x in array if func(x)]
    else:
        yield from [x for x in array if x]
