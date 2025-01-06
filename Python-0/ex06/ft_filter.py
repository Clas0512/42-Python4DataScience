def ft_filter(func: callable, array: iter):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    """
    if func:
        yield from [x for x in array if func(x)]
    else:
        yield from [x for x in array if x]
