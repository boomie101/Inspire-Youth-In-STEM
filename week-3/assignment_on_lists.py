#create an empty list of your fav musicians
#using for_loop add 5 new musicians
#copy the list to a new list named celebs
#sort the list 
#pop out 2 celebs
#count the remaining celebs in the lists 
fav_artists = [ ]
fav_persons = ("Kid Laroi" , "YNW" , "PEEP" , "KSI" , "Breezy")
for fav_person in fav_persons:
    fav_artists.append(fav_person)
    print(fav_artists)
celebs = fav_artists.copy()
print(celebs)
celebs.sort()
print(celebs)
celebs.pop()
print(celebs)
celebs.pop()
print(celebs)
print(len(celebs))