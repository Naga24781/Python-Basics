friends={"Naga","Ravi", "Suraj", "Ravi", "Karthik"}
print(friends)
friends.remove("Ravi")
print(friends)
friends.add("Rakesh")
friends.add("Ram")
print(friends)
college_friends ={"Sarath","Guru","Kesav","Pilla Srinu","Rakesh"}

print("My Friend List",friends | college_friends)
print("Intersection",friends & college_friends)
print("Only College Friends:", college_friends - friends)
print("Only My Friends:", friends - college_friends)
