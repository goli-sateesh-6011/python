import os
if os.path.exists("Hello.txt"):
    os.remove("Hello.txt")
else:
    print("The file is not presnet")
