user_info = {
    'name' : 'prateek',
    'age' : 45,
    'fav_movies' : ['coco','coco','mario']
}
print(type(user_info))
#if 45 in user_info.values():
    #print('present')
#else:
    #print("not present")
user_items = user_info.items()
print(user_items)
[('name','Pratek'),('age',45),('fav_movies' , ['coco','coco','mario'])] 
for key, value in user_info.items():
    print(f"key is {key} and value is {value}")  