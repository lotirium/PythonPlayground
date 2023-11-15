def do_stuff(num=0):
    try:
        if num or num == 0:
            return int(num)+5
        else:
            return 'please return a number'
    except ValueError as err:
        return err


test_param = -1
print(do_stuff(test_param))
