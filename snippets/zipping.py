def main():
    names = ['Eric Idle', 'John Cleese', 'Graham Chapman']
    ages = [42, 76, 9]

    as_list = get_ids_as_list(names, ages)
    print(as_list)
    as_dict = get_ids_as_dict(names, ages)
    print(as_dict)


def get_ids_as_list(names, ages):
    ids = list()
    for name, age in zip(names, ages):
        ids.append(''.join([get_initials(name),str(age)]))
    return ids


def get_ids_as_dict(names, ages):
    '''
    NOTE: second occurance of a name will be ignored
    '''
    ids = dict()
    for name, age in zip(names, ages):
        initials = get_initials(name)
        if ids.get(initials) is None:
            ids[initials] = age
    return ids


def get_initials(name):
    '''
    just works for a name in the format first last,
    will fail for any name with more then 1 empty space in it.
    '''
    first, last = name.split()
    return ''.join([first[0], last[:2]]).upper()


if __name__ == '__main__':
    main()
