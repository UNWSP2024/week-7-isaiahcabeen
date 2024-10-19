def main():
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print('Number:', number)

    print('List of numbers:')
    print(f'{number_list}')

    print(f'List of numbers that are larger than {number}:')

    display_larger_than_n_list(number, number_list)

def display_larger_than_n_list(n, n_list):
    for num in n_list:
        if num > n:
            print(num)

if __name__ == '__main__':
    main()
