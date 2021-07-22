from kahoot import client
from sys import argv
from threading import Thread


def get(int_range, id):
    for i in int_range:
        if cl.join(i, 'Kahoot-Police') is not False:
            print(i)
    print(str(id) + ' is DONE!')


ranges = list(range(int(argv[1].split('-')[0]), int(argv[1].split('-')[1])))
ranges = [ranges[i:i+250] for i in range(0, len(ranges), 250)]


cl = client()
id = 0

for i in ranges:
    id += 1
    Thread(target=get, args=(i,id)).start()
print(f'Started {id} Threads')
