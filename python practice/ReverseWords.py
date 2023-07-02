str1 = 'Hello there world'

def reverse1(strIn : str):
    listOut = strIn.split()      # find spaces and split and reverse (too easy?)
    listOut.reverse()
    strOut = ' '.join(listOut)             # list-to-string NB join prefixing each list element with ' '
    return strOut


def reverse2(strIn : str):
    splitten = strIn.split()
    strOut = splitten[::-1]        # splice from start:to end:move backwards [in array]
    return strOut

def reverse3(strIn : str):
    listOut = strIn.split()      # find spaces and split and reverse (too easy?)
    listOut.reverse()
    strOut = ' '.join([str(item) for item in listOut])             # list comprehension within join in [] NB join prefixing each list element with ' '
    return strOut



print(f'reverse1 {reverse1(str1)}')
print(f'reverse2 {reverse2(str1)}')
print(f'reverse3 {reverse3(str1)}')
