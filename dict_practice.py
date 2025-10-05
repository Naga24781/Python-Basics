friends_age = {
    "Rakesh Age" :24,
    "Ram Age":23,
    "Naga Age" :20
}
print(friends_age)
friends_age["Guru Age"]=25
friends_age["Ram Age"]=22
print(friends_age)
friends_age.pop("Naga Age")
print(friends_age)
for key,value in friends_age.items():
    print(key,":",value)


    