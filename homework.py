import time 
import asyncio
import urllib
import json
from urllib import request

user = []
user_albums = []
user_posts = []
user_id = 0
default_url = 'https://jsonplaceholder.typicode.com/'

#Without async

def user_info_load():
    for i in range(1,11):
        user_id = i
        user_posts = list(request.urlopen(default_url + f'users/{user_id}/posts/'))
        user.append(list(user_posts))
        user_todos = list(request.urlopen(default_url + f'users/{user_id}/todos/'))
        user[i-1].append(list(user_todos))
        user_albums = list(request.urlopen(default_url + f'users/{user_id}/albums/'))
        user[i-1].append(list(user_albums))

start = time.time()
user_info_load()
print(f'Without async {time.time() - start}')

async def user_info_load():
    for i in range(1,11):
        user_id = i
        user_posts = list(request.urlopen(default_url + f'users/{user_id}/posts/'))
        user.append(list(user_posts))
        user_todos = list(request.urlopen(default_url + f'users/{user_id}/todos/'))
        user[i-1].append(list(user_todos))
        user_albums = list(request.urlopen(default_url + f'users/{user_id}/albums/'))
        user[i-1].append(list(user_albums))

async def user_load_info_main():
    asyncio.gather(user_info_load())

'''
Without async 7.557633876800537
Async 7.864319801330566
'''

start = time.time()
asyncio.run(user_load_info_main())
print(f'Async {time.time() - start}')

def albums_info_load():
     for i in range(1,11):
         user_id = i
         photos = list(request.urlopen(default_url + f'albums/{user_id}/photos/'))
         user_albums.append(photos)
        
start = time.time()
albums_info_load()
print(f'Without async {time.time() - start}')

async def albums_info_load():
     for i in range(1,11):
         user_id = i
         photos = list(request.urlopen(default_url + f'albums/{user_id}/photos/'))
         user_albums.append(photos)
        
async def albums_info_load_main():
    asyncio.gather(albums_info_load())

start = time.time()
asyncio.run(albums_info_load_main())
print(f'Async {time.time() - start}')

'''
Without async 3.857109546661377
Async 2.807009696960449
'''

def posts_info_load():
     for i in range(1,11):
         user_id = i
         comments = list(request.urlopen(default_url + f'albums/{user_id}/comments/'))
         user_albums.append(comments)
        
start = time.time()
posts_info_load()
print(f'Without async {time.time() - start}')

async def posts_info_load():
     for i in range(1,11):
         user_id = i
         comments = list(request.urlopen(default_url + f'albums/{user_id}/comments/'))
         user_albums.append(comments)
        
async def posts_info_load_main():
    asyncio.gather(posts_info_load())

start = time.time()
asyncio.run(posts_info_load_main())
print(f'Async {time.time() - start}')

'''
Without async 7.3381428718566895
Async 6.101698637008667
'''


