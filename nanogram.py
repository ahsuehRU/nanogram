from itertools import izip_longest

def read_image(pic):
    rows = pic.split('\n')
    cols = (''.join(x) for x in izip_longest(*rows, fillvalue=' '))
    count = lambda lines: [[str(len(set)) for set in line.split()] for line in lines]
    return count(rows), count(cols)

def format_count(count):
    maxlen = max(len(x) for x in count)
    digit = max(max(len(y) for y in x) for x in count)
    count = ([y.rjust(digit) for y in x] for x in count)
    maxspc = ' '*digit
    
    #maxSpace = max(len(x) for x in count)
    return [[maxspc]*(maxlen-len(x)) + x for x in count]

def print_counts(pic):
    
    rows, cols = read_image(pic)
    print rows, cols
    rows = format_count(rows)
    cols = format_count(cols)
    #rows
    newRows = [' '.join(x) for x in rows]
    pad = max(len(x) for x in newRows)

    #cols
    newCols =[' '.join(x) for x in zip(*cols)]

    for x in newCols:
        print ' '*pad + x

    print '\n'.join(newRows)




pic ="    *\n   **\n  * *\n *  *\n*****"
pic_2="    ** *\n   *****\n  ******\n ********\n**********\n *      *\n * ** * *\n * ** * *\n * **   *\n ********"
print pic_2
print_counts(pic_2)
