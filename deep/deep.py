def main():

    s = input('What is the Answer to the Great Question of Life, the Universe, and Everything?').casefold().strip()
    #s = s.ca
    if s == 'forty two' or s == 'forty-two' or s == '42':
        print('Yes')
    else:
        print('No')

main()