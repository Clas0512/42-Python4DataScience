def ft_tqdm(lst: range):
    """
    Custom implementation of a progress bar for iterating over a list or range
    of items.

    Args:
        lst (range): A range or iterable for which progress needs to be shown.

    Yields:
        item: The next item in the iterable.

    This function simulates the behavior of the 'tqdm' library by displaying a
    progress bar. The progress bar shows the percentage completed and the
    number of items processed out of the total.

    Example:
        >>> for i in ft_tqdm(range(100)):
        >>>     # Perform operations here
    """
    length = 95
    total = lst.stop - lst.start

    i = 0
    for item in lst:
        i += 1
        percentage = i * 100 // total
        filled_length = length * i // total
        bar = '█' * filled_length + ' ' * (length - filled_length)
        if (i % 20 == 0 or i == total):
            print(f"\r{percentage:3d}%|{bar}| {i}/{total:3d}", end="")
        yield item
