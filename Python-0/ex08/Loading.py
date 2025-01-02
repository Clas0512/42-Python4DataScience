def ft_tqdm(lst: range) -> None:
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