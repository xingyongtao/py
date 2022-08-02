def extract(raw):
    name = ''
    count = 0
    for ch in raw:
        if ch.isdigit():
            count = count*10+int(ch)
        else:
            name += ch
    return (name, count)


def split_cell(raw):
    tokens = raw.split(',')
    res = []
    for token in tokens:
        # print('token is {}'.format(token))
        if token == '':
            continue
        res.append(extract(token))
    return res
