fname = input('Enter file name: ')
fhandle = open(fname)
for text in fhandle:
    x = text.rstrip()
    print(x.upper())
