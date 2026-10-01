list= [ "apple", "banana","orange","guava"]

# ADD
def add():
  i= input(" enter the item to be added : ")
  list.append(i)

  for item in list :
   print(item)
  
# view 
def view() :
 for item in list:
   print(item)

# view()

# update 
def update():
 i= input(" enter the item to be replaced : ")
 n= input("enter the item by which its replaced: ")
 for item in list :
    if item == i :
      no = list.index(item)
      list[no]=n
      print(list)

# delete 
def delete():
  i= input("enter any item from the list to be deleted : ")
  for item in list :
    if item == i : 
      list.remove(item)
      print(list)

# exit 
def exit():
      i =input("enter e to exit: ")
      if i.lower() == "e":
        return True 


# function call

while True:
  v1= input (" Enter 1 to view,2 to add ,3 to update ,4 to delete and 5 to exitː ")

  if v1=="1":
        view()

  elif v1== "2":
     add()
  elif v1=="3":
    update()
  elif v1=="4":
   delete()
  elif v1=="5":
    while exit() is True :
       break