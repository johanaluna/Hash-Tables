import random
def howmany_before_collision(buckets, loops=1):
    for i in range(loops):
        tries = 0 
        tried=set()
        tried_list = []

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                break
        print(f'{buckets} buckets, tries {tried_list}')
howmany_before_collision(10,1)