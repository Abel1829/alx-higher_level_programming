#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def rep(a):
        return (a if a != search else replace)
    return list(map(rep, my_list))
