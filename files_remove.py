import os
if os.path.exists("anatomy_102.txt"):
    os.remove("anatomy_102.txt")
else:{
    print("the file does not exist")
}