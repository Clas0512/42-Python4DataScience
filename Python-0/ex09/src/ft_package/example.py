from ft_package import count_in_list

if __name__ == "__main__":
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0