
f = open("Hello.txt","a")
print("\n")
f.write("\nNow the file has more content!")
f.close()

#open and read the file 
f = open("Hello.txt","r")
print(f.read()) 