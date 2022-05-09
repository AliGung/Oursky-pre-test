#!user/bin/env python

import sys
import time
import math

cache = {}      
last_access_time = {}
key_weight = {}
current_time = 0.0

capacity = 360  # set to preference


def get(key):       
    if (key in cache):
        last_access_time[key] = time.time()              # record access time if the key exists in dictionary
    return cache.get(key,-1)
                                                         # computational complexity of get(): O(1) on average, O(n) for worst case

def put(key,value,weight):
    global last_access_time
    global cache
    global key_weight
    global current_time
    current_time =last_access_time[key] = time.time()   # record time for each access
    cache[key] = value  
    key_weight[key] = weight

    if sys.getsizeof(cache) > capacity:                 # when exceed desired capacity
        key_score = score()
        z = dict(sorted(key_score.items(),key =lambda kv:(kv[1], kv[0])),reverse=True)      # O(n log n) for sort, O(n) for reverse
        
        key_score.clear()
        key = (z.popitem(0))[0]                         # find key of popitem
        cache.pop(key)  
        last_access_time.pop(key)
        key_weight.pop(key)                             # O(1) for pop
        
        temp = {}
        temp.update(cache)                              # use update to get dictionary of smaller capacity
        cache = temp
        temp = {}
        temp.update(last_access_time)
        last_access_time = temp
        temp = {}
        temp.update(key_weight)
        key_weight = temp                               # O(1) for update

        

def score():
    global key_weight
    key_score = {}
    x=list(key_weight.values())
    y=list(key_weight.keys())
    
    for i in range(len(key_weight)):                    # O(n) for For loop
        weight = x[i]
        key = y[i]
        if current_time != last_access_time[key]:
            key_score[key] = weight / math.log((current_time - last_access_time[key]) + 1)
        else:
            key_score[key] = weight / -100
        
    return key_score
    

# While not reaching capacity, put() function has complexity = O(1)
# When reaching capacity, put() has complexity: O(n) + O(n log n) + O(n) = O(2n) + O(n log n)
# where n = len(key_weight) = len(cache)   



