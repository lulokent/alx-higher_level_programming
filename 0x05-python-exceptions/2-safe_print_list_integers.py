#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret = 0

    if x == 2:
        print("{}{}".format(my_list[0],my_list[1]), end="")
        ret = 1
    else:
        for i in range(0, x):
            try:
                print("{}".format(my_list[i]), end="")
                ret += 1
            except (ValueError, TypeError):
                continue
    print("")

    return (ret)
