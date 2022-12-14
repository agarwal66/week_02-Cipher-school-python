user_info = {
    'name' : 'Prateek',
    'age' : 23,
    'fav_movies' : ['coco','marvel','mario'],
    'fav_tunes' : ['awakeninh','fairy tales']
}
#user_info['fav_songs'] = ['song1','song2']
#print(user_info)
popped_item = user_info.pop('fav_tunes')
print(user_info)
popped_item = user_info.popitem()
print(user_info)
print(type(user_info))