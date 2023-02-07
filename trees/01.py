def insert(raiz, data):
    if raiz is None:
        return {'data': data, 'left': None, 'right': None}
    else:
        current = raiz
        while True:
            if data < current['data']:
                if current['left'] is None:
                    current['left'] = {'data': data, 'left': None, 'right': None}
                    break
                else:
                    current = current['left']
            elif data > current['data']:
                if current['right'] is None:
                    current['right'] = {'data': data, 'left': None, 'right': None}
                    break
                else:
                    current = current['right']
            else:
                break
    return raiz

def search(raiz, data):
    current = raiz
    while current is not None:
        if data < current['data']:
            current = current['left']
        elif data > current['data']:
            current = current['right']
        else:
            return current['data']
    return None

def in_order_traversal(raiz):
    if raiz is not None:
        in_order_traversal(raiz['left'])
        print(raiz['data'])
        in_order_traversal(raiz['right'])
    return raiz['data']

raiz = None
while True:
    n = input()
    try:
        n = int(n)
        raiz = insert(raiz, n)
    except ValueError:
        if n == 'in':
            result = in_order_traversal(raiz)
            print(result)
        if n == 'quack':
            break
        