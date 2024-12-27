def ft_filter(func: callable, array: iter):
    if func:
        yield from [x for x in array if func(x)]
    else: 
        yield from [x for x in array if x]
