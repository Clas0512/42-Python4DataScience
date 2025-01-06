def printStr(object, str):
    print(f'{str}: {object} {type(object)}')

def NULL_not_found(object: any) -> int:
    if object is None:
        printStr(object, 'Nothing')
    elif type(object) is float and object != object:
        printStr(object, 'Cheese')
    elif type(object) is int and object == 0:
        printStr(object, 'Zero')
    elif type(object) is str and len(object) == 0:
        printStr(object, 'Empty')
    elif type(object) is bool and object == False:
        printStr(object, 'Fake')
    else:
        print('Type not Found')
        return (1)
    return (0)