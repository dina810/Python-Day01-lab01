index=range(5)
user_list=[]
for i in index:
    user_list.append(int(input("plz enter number")))
user_list.sort()
print("Sort in ascending: " , user_list)
user_list.sort(reverse=True)
print("Sort in descending: " , user_list)

