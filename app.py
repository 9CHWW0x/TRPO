from calc import calc_line

if __name__ == '__main__':
    line = '+ 6 7'
    res = calc_line(line)
    print("{} = {}".format(line, res))
