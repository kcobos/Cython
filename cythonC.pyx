from libc.stdlib cimport atoi

cdef parse_charptr_to_py_int(char* s):
    assert s is not NULL, "string is NULL"
    return atoi(s)

def string_to_int(n):
    return parse_charptr_to_py_int(n)
