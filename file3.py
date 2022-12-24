# import os
# if os.path.exists("img3.png"):
#     os.rename("img3.png","img4.png")
# else:
#     print("File does not exits")



# import os
# if os.path.exists("DEMO2.txt"):
    # os.remove("DEMO2.txt")
# else:
    # print("file does not exist")

# try:
# this block of code will run and throw errors if there are any error

# except - this will raise the error 
# else - this will exicute if there is no error
# finally - this will execute regardless the result of try and except
try:
    f=open("demo.txt")
    try:
        # f.close()
        f=open("img4.png","rb")
        print(f.read())
    except:
        print("Error in file")
    finally:
        print("Gaurav")
except:
    print("Error in bahar wali line file")